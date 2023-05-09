# nexora
Next Explora - yet another machine learning library

1) [Quick Start Guide](#quick-start-guide)
    + [Installing and Activating Environment](#installing-and-activating-environment)
    + [Building and Installing Package](#building-and-installing-package)
    + [Clean conda environment](#clean-conda-environment)
2) [Docker Image](#docker-image)
    + [Building Docker Image](#building-docker-image)
    + [Running Docker Contaier](#running-docker-container)
3) [Tests and Documents](#tests-and-documents)
    + [Running Unit Tests](#running-unit-tests)
    + [Generating the Documents](#generating-the-documents)
    + [Code Quality Checks](#code-quality-checks)
4) [Cli Usage](#cli-usage)
    + [Training model](#training-model)
    + [Monitoring optimization](#monitoring-optimization)
    + [Explaining model](#explaining-model)
    + [Predicting file using model](#predicting-file-using-model)
    + [Serving model](#serving-model)
5) [Publish](#publish)
    + [Publishing python package](#publishing-python-package)
    + [Publishing docker image](#publishing-docker-image)
6) [Docker Additional](#docker)
    + [Training on docker](#training-on-docker)
    + [Monitoring on docker](#monitoring-on-docker)
    + [Explain on docker](#explain-on-docker)
    + [Prediction on docker](#prediction-on-docker)
    + [Serving on docker](#serving-on-docker)


## Quick Start Guide

- Train `xgboost` or `lightgbm` models optimizing `optuna`. Refactored [autoxgb](https://github.com/abhishekkrthakur/autoxgb) package!
- Select Features using [boruta](https://github.com/scikit-learn-contrib/boruta_py)
- Monitor optimization studies using [optuna-dashboards](https://github.com/optuna/optuna-dashboard)
- Explain the final models using [shapash](https://github.com/MAIF/shapash)
- `nexora` is available on [github](https://github.com/overenginar/nexora), [dockerhub](https://hub.docker.com/repository/docker/overenginar/nexora/general) and [pypi](https://pypi.org/project/nexora/)

### Installing and Activating Environment

```shell
conda env create -f environment.yaml
conda activate nexora_env
```

### Building and Installing Package

```shell
make install version=0.0.1
```

```python
import nexora
```

> Alternative1: `pip insall -e .`

> Alternative2: `python setup.py sdist`

### Clean conda environment

```shell
conda env remove -n nexora_env
```

## Docker Image

### Building Docker Image

```shell
mkdir ~/nexora_data
```

```shell
docker compose build
```

### Running Docker Container

```shell
docker compose up -d --no-build
```
> Jupyter Notebook: http://localhost:8901 [Pwd: welcome1]

> Sphinx docs: http://localhost:8902

## Tests and Documents

### Runing Unit Tests

```shell
make tests
```

> Alternative: `python -m tests.test3.test_runner`

### Generating the Documents

```shell
make docs
```

> http://localhost:5001

> Generate Docs: `sphinx-quickstart --sep -p nexora -a="Ali Cabukel" -v=0.0.1 -r=0.0.1 -l=en`

### Code Quality Checks

```shell
make quality
```

## CLI Usage

### Training model

```shell
nexora train --algo=xgb \
        --fs=1 \
        --train_filename ./data_samples/binary_classification.csv \
        --output binary-xgb-study-1 \
        --targets income \
        --num_folds 5 \
        --num_trials 100 \
        --time_limit 360 \
        --seed 42
```

### Monitoring optimization

```shell
nexora monitor --db_path=sqlite:///binary-xgb-study-1/params.db
```

> Alternative: `optuna-dashboard sqlite:///params.db`

### Explaining model

```shell
nexora explain --model_path=binary-xgb-study-1/atuna_model.0 \
        --data_path=binary-xgb-study-1/valid_fold_0.feather \
        --config_path=binary-xgb-study-1/atuna.config \
        --features_path=binary-xgb-study-1/selected_features.json
```

### Predicting file using model

```python
import pandas as pd

df = pd.read_csv('data_samples/binary_classification.csv')
df['id'] = list(range(1, df.shape[0] + 1))
df.to_csv('binary-xgb-study-1/predictions_data.csv', index=False)
```

```shell
nexora predict --model_path=binary-xgb-study-1 \
        --test_filename=binary-xgb-study-1/predictions_data.csv  \
        --out_filename=binary-xgb-study-1/predictions.csv
```

### Serving model

```shell
nexora serve --model_path=binary-xgb-study-1
```

> Example data, output: `<=50K`
```json
{
  "workclass": "Private",
  "education": "HS-grad",
  "marital.status": "HS-grad",
  "occupation": "Handlers-cleaners",
  "relationship": "Unmarried",
  "race": "Black",
  "sex": "Female",
  "native.country": "United-States",
  "age": 24,
  "fnlwgt": 82804,
  "education.num": 9,
  "capital.gain": 0,
  "capital.loss": 0,
  "hours.per.week": 40
}
```

> http://localhost:9999/docs

## Publish

### Publishing python package

```shell
twine upload dist/*
```

### Publishing docker image

```shell
docker build -t overenginar/nexora:latest .
# docker run -i -t -p 8901:8888 -p 8902:5001 -p 8903:8080 -p 8904:8050 -p 8905:9999 --name nexora-dev overenginar/nexora:latest
docker push overenginar/nexora:latest
```

## Docker Additional

```shell
docker run -i -t -p 8901:8888 -p 8902:5001 -p 8903:8080 -p 8904:8050 -p 8905:9999 --name nexora-dev overenginar/nexora:latest
```

```shell
docker ps | grep nexora-dev
```

### Training on docker

```shell
docker exec -it nexora-dev conda run -n nexora_env nexora train --algo=xgb \
        --fs=1 \
        --train_filename ./examples/data_samples/binary_classification.csv \
        --output binary-xgb-study-1 \
        --targets income \
        --num_folds 5 \
        --num_trials 100 \
        --time_limit 360 \
        --seed 42
```

### Monitoring on docker

```shell
docker exec -it nexora-dev ls binary-xgb-study-1
```

```shell
docker exec -it nexora-dev conda run -n nexora_env nexora monitor --db_path=sqlite:///binary-xgb-study-1/params.db
```

> Optuna Dashboard: http://localhost:8903

### Explain on docker

```shell
docker exec -it nexora-dev conda run -n nexora_env nexora explain --model_path=binary-xgb-study-1/atuna_model.0 \
        --data_path=binary-xgb-study-1/valid_fold_0.feather \
        --config_path=binary-xgb-study-1/atuna.config \
        --features_path=binary-xgb-study-1/selected_features.json
```

> Shapash Explanations: http://localhost:8904

### Prediction on docker

```python
import pandas as pd

df = pd.read_csv('data_samples/binary_classification.csv')
df['id'] = list(range(1, df.shape[0] + 1))
df.to_csv('binary-xgb-study-1/predictions_data.csv', index=False)
```

```shell
docker exec -it nexora-dev conda run -n nexora_env nexora predict --model_path=binary-xgb-study-1 \
        --test_filename=binary-xgb-study-1/predictions_data.csv  \
        --out_filename=binary-xgb-study-1/predictions.csv
```

```shell
docker exec -it nexora-dev head binary-xgb-study-1/predictions.csv
```

### Serving on docker


```shell
docker exec -it nexora-dev conda run -n nexora_env nexora serve --model_path=binary-xgb-study-1
```

> FastAPI Serving: http://localhost:8905/docs

```shell
docker exec -it nexora-ml-1 curl -X 'POST' \
  'http://localhost:9999/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"workclass": "Private", "education": "HS-grad", "marital.status": "HS-grad", "occupation": "Handlers-cleaners", "relationship": "Unmarried", "race": "Black", "sex": "Female", "native.country": "United-States", "age": 24, "fnlwgt": 82804, "education.num": 9, "capital.gain": 0, "capital.loss": 0, "hours.per.week": 40 }'
```
