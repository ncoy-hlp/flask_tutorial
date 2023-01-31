#!/bin/bash
docker run -it --rm --name cerbot \
-v ${PWD}/letsencrypt/:/letsencrypt \
-v ${PWD}/letsencrypt/certs/:/etc/letsencrypt \
certbot:latest renew

docker exec nginx nginx -s reload
