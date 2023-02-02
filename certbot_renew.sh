#!/bin/bash
cd /home/ncoy/app/flask_tutorial
docker run --rm --name cerbot \
-v ${PWD}/letsencrypt/:/letsencrypt \
-v ${PWD}/letsencrypt/certs/:/etc/letsencrypt \
certbot:latest 

docker exec nginx nginx -s reload
