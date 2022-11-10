# CatMeIfYouCan

The world's best cat pictures API

## Technology Stack

- Python
- Django
- Django REST Framework
- Coverage
- Psycopg2
- Gunicorn
- NGINX
- PostgreSQL
- Docker

## Get Started

To run this API, it is required to use Docker with Docker-Compose. The following modes are supported while running the API:

- Development
- Production

The difference between Development and Production is that Production mode will have:
- the Django `DEBUG` setting turned off,
- the way in which static and media files are handled will vary, and
- NGINX will be used along-with Gunicorn for serving the API.

### Development

To run the API in "Development" mode, use the following set of commands:

```bash
docker-compose up --detach --build
```

### Production

To run the API in "Production" mode, use the following set of commands:

```bash
docker-compose -f docker-compose.production.yml up --detach --build
```
```bash
docker-compose -f docker-compose.production.yml exec server python manage.py migrate --noinput
```
```bash
docker-compose -f docker-compose.production.yml exec server python manage.py collectstatic --no-input --clear
```

## API Documentation

| End-Point | HTTP Method | CRUD Method | Notes |
|:---|:---:|:---:|:---|
| `/api/pictures` | `POST` | Create | Create a new cat picture |
| `/api/pictures` | `GET` | Read | Read all cat pictures |
| `/api/pictures/:id` | `GET` | Read | Read cat picture with particular ID |
| `/api/pictures/:id` | `PUT` | Update | Update cat picture with particular ID |
| `/api/pictures/:id` | `DELETE` | Delete | Delete cat picture with particular ID |

## Overview

Your task is to build a RESTful API for uploading and managing cat pictures.

## Requirements

Your API MUST support the following operations:

- [x] Upload a cat pic.
    - `POST` request
- [x] Delete a cat pic.
    - `DELETE` request
- [x] Update a previously uploaded cat pic (not just metadata) in place.
    - `PUT` or `PATCH` request
- [x] Fetch a particular cat image file by its ID.
    - `GET` request
    - `/cats/{id}`
- [x] Fetch a list of the uploaded cat pics.
    - `GET` request
    - `/cats` end-point

Additionally, you MUST:

- [x] Correctly use HTTP response codes, including error handling.
- [x] Provide documentation for your API's behavior.
- [x] Provide instructions for us to get your API up and running.
- [x] Write a basic suite of tests for your code.

## Suggestions

If you want to show off a little bit, do one or more of the following:

- [x] Dockerize your application, it's okay if your pictures aren't persisted outside of the container runtime.
- [x] Setup authentication/authorization
