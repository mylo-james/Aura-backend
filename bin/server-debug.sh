#!/bin/bash

export FLASK_APP=server.py
export FLASK_ENV=development

flask run --port 5000
