# pull official base image
FROM python:latest

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install updates
RUN apt-get update && apt-get upgrade -y

# install packages
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# set source
COPY ./src /src
WORKDIR /src
