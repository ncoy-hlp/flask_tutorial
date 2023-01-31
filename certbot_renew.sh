#!/bin/bash
docker run --rm --name cerbot \
-v ${PWD}/letsencrypt/:/letsencrypt \
-v ${PWD}/letsencrypt/certs/:/etc/letsencrypt \
certbot:latest 

docker exec nginx nginx -s reload
