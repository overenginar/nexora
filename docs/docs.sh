rm -rf build
make html
export FLASK_APP=app.py
export FLASK_DEBUG=1
python -m flask run --host=localhost --port=5001
