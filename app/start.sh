#!/bin/bash
flask db upgrade
gunicorn -w 3 --bind 0.0.0.0:8000 app:app