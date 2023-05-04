FROM continuumio/anaconda3:latest

RUN apt-get update --yes --quiet && DEBIAN_FRONTEND=noninteractive apt-get install --yes --quiet --no-install-recommends \
    software-properties-common \
    build-essential apt-utils \
    wget curl vim git ca-certificates kmod \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /nexora

COPY . .

RUN conda env create -f environment.yaml && \
    . /opt/conda/bin/activate && \
    conda activate nexora_env && \
    make install version=0.0.1

EXPOSE 8888/tcp 5001/tcp

COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ENTRYPOINT make docs && jupyter-lab --notebook-dir=/nexora --ip=* --port=8888 --no-browser --allow-root
