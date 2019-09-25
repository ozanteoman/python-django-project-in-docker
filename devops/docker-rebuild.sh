#!/usr/bin/env bash
docker-compose  build --no-cache --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY --build-arg AWS_S3_CUSTOM_DOMAIN=$AWS_S3_CUSTOM_DOMAIN --build-arg AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME && docker-compose up
