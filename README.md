# Webhook registration app

## Goal
Create an application that registers webhooks and triggers all registered webhooks on request

## Prerequisites
- python3
- Django
- Docker

### Run application
- Create your env file `.env` in the project folder and add your prefered webhook token in this format `WEBHOOK_TOKEN=45a9eef987caa53c07a433c2daf58728`
- Build the docker image with `docker-compose build`
- Run migrations with `docker-compose run webhookserver sh -c "python webhookserver/manage.py makemigrations"`
followed by `docker-compose run webhookserver sh -c "python webhookserver/manage.py migrate"`
- Run the application with `docker-compose up`
#### Running tests
- Create a virtual env with `python3 -m venv env`
- Activate the virtual env
- Install dependencies with `pip install -r /requirements.txt`
- Run tests with `pytest`

### Endpoints
#### Add webhook
- url is `/api/webhook/`
- Exple request
    `POST /api/webhook/ HTTP/1.1
    Host: 0.0.0.0:9876
    Content-Type: application/json
    webhook-token: 45a9eef987caa53c07a433c2daf58728
    Accept: */*
    Content-Length: 81
    | {
    | 	"url": "http://0.0.0.0:3000/reporting",
    | 	"status": "ACTIVE",
    | 	"token":"foo"
    | }`

#### Trigger webhook
- url is `/api/webhook/test/`
- Exple request
    `POST /api/webhook/ HTTP/1.1
    Host: 0.0.0.0:9876
    Content-Type: application/json
    Accept: */*
    Content-Length: 81
    | {
    | 	"payload": ["any", {"valid":"json"}]
    | }`

### Pending work
- Add more tests
- Add documentation
- Move the triggering of the webhooks into a celery task
- Add logging

### Limitations
- Solution is not suitable for production because the token used is very simple
