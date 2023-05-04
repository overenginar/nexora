#!/bin/bash
conda activate nexora_env
rm -rf build
make html
FLASK_APP=app.py nohup flask run --host=localhost --port=5001 > log.txt 2>&1 &
