# bikeshare

An app designed to pair riders with bikes. Built with [Django](https://www.djangoproject.com/), [Django Rest Framework](https://www.django-rest-framework.org/), and [Graphene-Python](https://graphene-python.org/).

## Prerequisites

Please ensure that you have the following installed:

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. ` git clone git@github.com:sarahgrossman/bikeshare.git`
1. `cd bikeshare`
1. `docker-compose up` (spin up DB and web containers)
1. `docker-compose exec web python manage.py migrate` (run migrations)

You should see logging in your terminal that indicates the development server is running on `http://0.0.0.0:8000/`.

## Setting up an account

Use the django-admin command to create a superuser: `docker-compose exec web python manage.py createsuperuser`

## Interacting with the REST API

Using cURL or Postman, you should be able to `GET http://localhost:8000/bicycles/` and `GET http://localhost:8000/users/<optional_user_id>`. The latter endpoint should return either a list containing one user (yours!) or a single object with your user info, depending on whether or not you pass your user ID.

Other views and methods are restricted based on admin and instance-specific permissions. In order to complete all requests, you will have to send your requests with an authentication header (see [Authentication](#authentication) below).

Django Rest Framework also provides a browsable API that can be accessed at http://127.0.0.1:8000/. Click the "Log in" prompt in the top righthand corner and enter your superuser credentials. You will then be able to send all API requests directly through this interface.

## Interacting with the GraphQL API

Visit http://127.0.0.1:8000/graphql to launch GraphiQL. This feature is a WIP.

## Interacting with the database

At any time you can enter the db container and launch psql by running `docker-compose exec db psql -U postgres`.

Django also offers its own admin site for CRUD operations on the database at http://127.0.0.1:8000/admin/. Your superuser login credentials should work here as well.

## Authentication

This project uses token-based authentication provided by [Django Rest Framework](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication).

To obtain your user token, send a POST request to `http://localhost:8000/api-token-auth/` with a JSON body containing your `username` and `password`.

For all subsequent requests, add a header `Authorization: Token <your_token_here>`.

## Running tests

From the root directory, run `docker-compose exec web python manage.py test`.
