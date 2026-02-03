#!/bin/bash
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8888
flask run --host=0.0.0.0 --port=8888
