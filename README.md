# COVID-19 UK Data REST API

A [REST API](https://covid-19-uk-api.dholmes.co.uk) for the UK COVID-19 data gathered by [tomwhite](https://github.com/tomwhite/covid-19-uk-data). There is also a [REST API](https://github.com/desholmes/covid-19-us-api) for the US COVID-19 data gathered by [nytimes](https://github.com/nytimes/covid-19-data).

## Docker Image Details

[hub.docker.com/repository/docker/desholmes/covid-19-uk-api](https://hub.docker.com/repository/docker/desholmes/covid-19-uk-api).

* Registry: desholmes
* Repository name: covid-19-uk-api
* Current version: 1.0.5

## Using the API

A hosted version version of the API can be found at [covid-19-uk-api.dholmes.co.uk](https://covid-19-uk-api.dholmes.co.uk).

The following starts a local server running on port 8000:

```bash
docker run -it -p 8000:8000 desholmes/covid-19-uk-api:1.0.3
```

| URL | Description | Hosted Link | Local Link |
| --- | --- | --- | --- |
| /uk/totals | All UK totals: tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/uk/totals/) | [local](http://0.0.0.0:8000/uk/totals/) |
| /uk/totals/?date=2020-03-15 | UK totals for date (`20-03-15`): tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/uk/totals/?date=2020-03-15) | [local](http://0.0.0.0:8000/uk/totals/?date=2020-03-15) |
| /uk/cases | Total cases by local authorities for the UK: country, area code, area and total cases | [hosted](https://covid-19-uk-api.dholmes.co.uk/uk/cases/) | [local](http://0.0.0.0:8000/uk/cases/) |
| /uk/cases/?date=20-03-15 | Total cases for date (`20-03-15`) by local authorities for the UK: country, area code, area, and total cases | [hosted](https://covid-19-uk-api.dholmes.co.uk/uk/cases/?date=20-03-15) | [local](http://0.0.0.0:8000/uk/cases/?date=20-03-15) |
| /scotland/totals | All Scotland totals: tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/scotland/totals/) |[local](http://0.0.0.0:8000/scotland/totals/) |
| /scotland/totals/?date=20-03-15 | All Scotland totals for date (`2020-03-15`): tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/?date=20-03-15) | [local](http://0.0.0.0:8000/scotland/totals/?date=20-03-15) |
| /wales/totals | All Wales totals: tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/wales/totals/) | [local](http://0.0.0.0:8000/wales/totals/) |
| /wales/totals/?date=2020-03-15 | All Wales totals for date(`2020-03-15`): tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/wales/totals/?date=2020-03-15) | [local](http://0.0.0.0:8000/wales/totals/?date=2020-03-15) |
| /northern-ireland/totals | All Northern Ireland totals: tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/northern-ireland/totals) | [local](http://0.0.0.0:8000/northern-ireland/totals/) |
| /northern-ireland/totals/2020-03-15 | All Northern Ireland totals for date (`2020-03-15`): tests, confirmed cases and deaths | [hosted](https://covid-19-uk-api.dholmes.co.uk/northern-ireland/totals/?date=2020-03-15) | [local](http://0.0.0.0:8000/northern-ireland/totals/?date=2020-03-15) |

## Getting Started (Development)

### Prerequisites

1. Installation of [Docker CE](https://store.docker.com/search?type=edition&offering=community)
1. Installation of [git SCM](https://git-scm.com/downloads)
1. Knowledge of [Python 3.7.3](https://www.python.org/downloads/)
1. Knowledge of [Django 3.0.8](https://www.djangoproject.com/)
1. Knowledge of [Django REST framework 3.11.0](https://www.django-rest-framework.org/)

Development takes place inside a docker container to:

1. Remove the need for a local virtual environment
1. Ensure the DEV environment is a close as possible to PROD

### Set up

1. Complete the 'Getting Started > Prerequisites' section
1. By default the app is configure for local development. Running `make build-cold` stand your local env up from scratch (not to be used for PROD)
1. Open [0.0.0.0:8000](http://0.0.0.0:8000/) in a browser to see the app running
1. Changing files in `covid_19_uk` will cause the app to reload
1. Press `CTL+c` to stop the docker container

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
* [Xavier Ordoquy (xordoquy)](https://medium.com/django-rest-framework/django-rest-framework-viewset-when-you-don-t-have-a-model-335a0490ba6f) and his [demo code](https://github.com/linovia/drf-demo) for creating a non-model Django REST API

## Version History

1. `1.0.5`: Bugfix for caching, added sma_7 & deaths_daily and updated to Django 3.0.7
1. `1.0.4`: Added CORS allow all headers, caching, ga tracking, GNU GENERAL PUBLIC V3 LICENSE
1. `1.0.3`: Added hosted API
1. `1.0.2`: Added default port
1. `1.0.1`: Added endpoints and docs for available data sources
1. `1.0.0`: Base repo with DBless Django app
