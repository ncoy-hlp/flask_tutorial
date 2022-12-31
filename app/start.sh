#!/bin/bash
flask db upgrade
flask run --debugger --host 0.0.0.0