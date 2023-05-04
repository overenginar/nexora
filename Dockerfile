FROM continuumio/anaconda3:latest

WORKDIR /opt/notebooks

COPY . .

EXPOSE 8888/tcp

ENTRYPOINT [ "jupyter-lab", "--notebook-dir=/opt/notebooks", "--ip=*", "--port=8888", "--no-browser", "--allow-root"]
