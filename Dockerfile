FROM python:3.7
MAINTAINER Tapasweni Pathak <tapaswenipathak@gmail.com>
EXPOSE 8000

WORKDIR /usr/src
RUN mkdir yourcfp
RUN cd yourcfp
WORKDIR /usr/src/yourcfp
COPY requirements.txt /usr/src/yourcfp/requirements.txt
RUN pip install -r requirements.txt

