#!/bin/bash
. /opt/conda/bin/activate
conda activate nexora_env
rm -rf build
make html
kill -9 $(lsof -t -i:5001)
FLASK_APP=app.py nohup flask run --host=0.0.0.0 --port=5001 > log.txt 2>&1 &
