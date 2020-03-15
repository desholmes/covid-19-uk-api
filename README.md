# COVID-19 UK Stats API

An API for the UK COVID-19 stats.

## Docker Image Details

[hub.docker.com/repository/docker/desholmes/covid-19-uk-api](https://hub.docker.com/repository/docker/desholmes/covid-19-uk-api).

* Registry: desholmes
* Repository name: covid-19-uk-api
* Current version: 1.0.0

## Using the API

england/totals/[date]
england/regions/[date]
northen-ireland/totals/[date]
wales/totals/[date]

## Getting Started

### Prerequisites

1. Installation of [Docker CE](https://store.docker.com/search?type=edition&offering=community)
1. Installation of [git SCM](https://git-scm.com/downloads)
1. Knowledge of [Python 3.7.3](https://www.python.org/downloads/)
1. Knowledge of [Django 3.0.4](https://www.djangoproject.com/)
1. Knowledge of [Django REST framework 3.11.0](https://www.django-rest-framework.org/)

## Development

Development takes place inside a docker container for the following reasons:

1. Removes the need for a local virtual environment
1. Ensures the DEV environment is a close as possible to PROD

### Set up

1. Complete the 'Getting Started > Prerequisites' section
1. By default the app is configure for local development. Running `make build-cold` stand your local env up from scratch (not to be used for PROD)
1. Open [0.0.0.0:8000](http://0.0.0.0:8000/) in a browser to see the app running
1. Changing files in `covid_19_uk` will cause the app to reload
1. Press CTL+c to stop the docker container

If you want to configure the application step-by-step follow the steps below:

1. Run `make setup`: To create the `.env` file from `.env-dist`
1. Configure the following in `.env`:
    1. **PORT**: The port the Django server will be exposed on (default 8000)
    1. **DEBUG**: Enable the app to run in development mode using `python3 manage.py runserver`, with live reloading of files changed in `covid_19_uk` (default 1)
    1. **DEV**: Enables [DEBUG](https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/) for the app (default 1)
    1. **QA**: Enables [flake8](https://pypi.org/project/flake8/) to be run against code on initial run, not live reload (default 1)
    1. **SECRET_KEY**: Secret key for the app, replace `add_me` with a random string (default 'add_me')
1. Run `make build`: To create the docker image
1. Run `make run`: To run the docker image as a container
1. Open [0.0.0.0:8000](http://0.0.0.0:8000/) in a browser to see the app running
1. The 2 above commands can be run using `make build-run`
1. Press CTL+c to stop the docker container

## Credits

* [Tome White (tomwhite)](https://github.com/tomwhite/covid-19-uk-data) for providing the data
* [Xavier Ordoquy (xordoquy)](https://medium.com/django-rest-framework/django-rest-framework-viewset-when-you-don-t-have-a-model-335a0490ba6f) and his [demo code](https://github.com/linovia/drf-demo) for non-model Django REST API

## Version History

1. `1.0.0`: Base repo with DBless Django app
