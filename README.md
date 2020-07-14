# bikeshare

An app designed to pair riders with bikes.

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
