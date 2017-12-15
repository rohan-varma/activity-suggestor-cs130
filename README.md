# CS 130 Project Notes

Location suggestor built for CS 130 by Elizabeth Muenchow, John Song, Aravind Sripathy, Lucas Tecot, Rohan Varma, and Henry Yang

[See this page on GitHub](https://github.com/rohan-varma/activity-suggestor-cs130/blob/master/README.md)


## Installation and running instructions

1) If you don't have Python3, install it using these instructions: http://docs.python-guide.org/en/latest/starting/install3/osx/

2) Clone the repository. 

3) Run `make install` to install the requirements with `pip3`. 

4) Run `make server` to run the server (alternatively, navigate to the `mysite/` directory and run `python3 manage.py runserver`)

5) Run `make tests` to run all of the tests (alternatively navigate to the `mysite/` directory and run `python3 manage.py test`)


## Workspace structure

| path | description |
| ---- | ----------- |
| `README.md` | this file |
| `requirements.txt` | list of pip package dependencies |
| `mysite/manage.py` | django management script |
| `mysite/mysite/` | django root (entry point) directory (which confusingly has the same name as the workspace root) |
| `mysite/placefindr/` | main backend <br/>`urls.py`: URL dispatch conf for backend services <br/>`views.py`: main dispatcher for backend "views" <br/>`place_recommender.py`: the location suggestor module <br/>`sharer.py`: the sharing module <br/>`settings.py`: python file loaded by the main django `settings.py`, contains backend settings and API keys <br> main front end <br> 'templates': directory contains django front-end templating logic |
| `mysite/placefindr/templates` | main UI <br/>`splash.html`: landing page <br/> `index.html`: map view|
| `mysite/placefindr/tests.py` | tests for backend |


### Run The Tests

`cd` into `mysite` and run `python3 manage.py test`

** Note ** about testing: The API tests require the server to be up and running in order to succeed. So use 2 terminals, and start the server with one of them, and then run the tests in the other. 

## Features & Web Interface

Main areas of functionality

* main UI
    * Splash Page: Entry point into app. Configure location preferences. 
    * Map View: Displays location information as well as ability to toggle through places. 
    * Google Maps embed, both for choosing a location & displaying suggestions
    * Google Calendar sharing
* places service (HTTP service serving data from Places, etc.)
    * Google Places API
* sharing service
    * Google Calendar

URLs

| URL | description |
| ---- | ----------- |
| `/` | directs to splash page |
| '/api/suggest/' | suggestion end point (only reachable from splash page) |

## Usage

Splash Page - Provide location of interest (autocomplete), entertainment type (tailored by group size), and radius. On submit, routed to main map view. <br>
Map View - Toggle through possible locations by clicking 'Try Somewhere Else'. Share location with friends by clicking share with friends button. Optionally redefine parameters by clicking 'Go Back'.



## Database stuff

Docs/source: https://docs.djangoproject.com/en/2.0/intro/tutorial02/#database-setup

Run migrations: python3 manage.py makemigrations placefindr

View migration: python3 manage.py sqlmigrate placefindr 0001
