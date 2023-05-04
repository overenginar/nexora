```shell
conda env list
conda create -n nexora_env python=3.7
conda activate nexora_env
pip install -r requirements.txt
````

```shell
conda env export > environment.yaml
```

```shell
conda deactivate
conda env remove -n nexora_env
conda env list
```

```shell
conda env create -f environment.yaml
```


```shell
pip insall -e .
```


```shell
python setup.py sdist
```

```shell
python -m build
```


```shell
docker build -t overenginar/nexora:latest .
# docker push overenginar/ds:latest
```

```shell
docker push overenginar/nexora:latest
```

```shell
docker run -i -t -p 8901:8888 --name nexora-dev overenginar/nexora:latest
```

```shell
sphinx-quickstart --sep -p nexora -a="Ali Cabukel" -v=0.0.1 -r=0.0.1 -l=en
```

```shell
cd docs
source docs.sh
```

```shell
python -m pytest tests/test1/test_dummy.py

python -m pytest tests/test2/test_dummy.py --param 1
```

```shell
python -m tests.test3.test_runner
```


```shell
python -m src.logger
python -m src.logger2
```


```shell
pre-commit install
pre-commit run --all-files
```
