# nexora
Next Explora - yet another machine learning library


## Quick Start Guide

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

### Building Docker Image

```shell
docker build -t overenginar/nexora:latest .
```

### Running Docker Container

```shell
docker run -i -t -p 8901:8888 -p 8902:5001 --name nexora-dev overenginar/nexora:latest
```
> http://localhost:8901
> http://localhost:8902

### Runing Unit Tests

```shell
make tests
```

### Generating the Documents

```shell
make docs
```

> http://localhost:5001

### Code Quality Checks

```shell
make quality
```

### Clean conda environment

```shell
conda env remove -n nexora_env
```

### Additional

```shell
pip insall -e .
python setup.py sdist
```

```shell
docker push overenginar/nexora:latest
```

```shell
sphinx-quickstart --sep -p nexora -a="Ali Cabukel" -v=0.0.1 -r=0.0.1 -l=en
```

```shell
python -m tests.test3.test_runner
```
