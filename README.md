# bikeshare

An app designed to pair riders with bikes. Built with [Django](https://www.djangoproject.com/) and [Django Rest Framework](https://www.django-rest-framework.org/).

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

Django Rest Framework also provides a browsable API that can be accessed at http://127.0.0.1:8000/. You should be able to log in (top righthand corner) with your superuser credentials and send API requests directly through this interface.

## Interacting with the GraphQL API

Visit http://127.0.0.1:8000/graphql to launch GraphiQL. This feature is a WIP.

## Interacting with the database

At any time you can enter the db container and launch psql by running `docker-compose exec db psql -U postgres`.

Django also offers its own admin site for CRUD operations on the database at http://127.0.0.1:8000/admin/. Your superuser login credentials should work here as well.

## Running tests

From the root directory, run `docker-compose exec web python manage.py test`.
