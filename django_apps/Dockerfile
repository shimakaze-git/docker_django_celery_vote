FROM python:3.8-alpine

# set working directory
WORKDIR /usr/src/app

# add app
COPY . /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install library settings
RUN apk --update add \
    gcc \
    libc-dev \
    tzdata \
    bash

# setting timezone
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pwd && ls -la

# Run Migration
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run Django Application
ENTRYPOINT ["python", "manage.py", "runserver"]
