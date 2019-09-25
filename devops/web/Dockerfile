FROM python:3.7
MAINTAINER Ozan Teoman DAYANAN

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_S3_CUSTOM_DOMAIN
ARG AWS_STORAGE_BUCKET_NAME

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_S3_CUSTOM_DOMAIN=$AWS_S3_CUSTOM_DOMAIN
ENV AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install ipython


COPY ./devops/web/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser --disabled-password user
USER user