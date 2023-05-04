```shell
conda env list
conda create -n nexora_env python=3.7
conda activate nexora_env
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