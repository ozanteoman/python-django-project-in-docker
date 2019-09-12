FROM python:3.7
MAINTAINER Ozan Teoman DAYANAN

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install ipython


COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser --disabled-password user
USER user