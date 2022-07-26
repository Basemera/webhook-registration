FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /webhookserver
WORKDIR /webhookserver
COPY . .
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt