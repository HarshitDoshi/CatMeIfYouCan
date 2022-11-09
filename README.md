# CatMeIfYouCan

The world's best cat pictures API

## Overview

Your task is to build a RESTful API for uploading and managing cat pictures.

## Requirements

Your API MUST support the following operations:

- Upload a cat pic.
    - `POST` request
- Delete a cat pic.
    - `DELETE` request
- Update a previously uploaded cat pic (not just metadata) in place.
    - `PUT` or `PATCH` request
- Fetch a particular cat image file by its ID.
    - `GET` request
    - `/cats/{id}`
- Fetch a list of the uploaded cat pics.
    - `GET` request
    - `/cats` end-point

Additionally, you MUST:

- Correctly use HTTP response codes, including error handling.
- Provide documentation for your API's behavior.
- Provide instructions for us to get your API up and running.
- Write a basic suite of tests for your code.

## Suggestions

If you want to show off a little bit, do one or more of the following:

- Dockerize your application, it's okay if your pictures aren't persisted outside of the container runtime.
- Setup authentication/authorization
