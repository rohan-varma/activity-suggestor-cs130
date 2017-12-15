# CS 130 Project Notes

Location suggestor built for CS 130 by Elizabeth Muenchow, John Song, Aravind Sripathy, Lucas Tecot, Rohan Varma, and Henry Yang

[See this page on GitHub](https://github.com/rohan-varma/activity-suggestor-cs130/blob/master/README.md)


## Instructions

To install all the requirements, run `pip[3] install requirements.txt`.

Run `python mysite/manage.py runserver` to start server. In order to run tests, please first `cd` into the outer `mysite` directory, before running `python manage.py test`; **otherwise test discovery will fail**.


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

## Features & Web Interface

Main areas of functionality

* main UI
    * Splash Page: Entry point into app. Configure location preferences. 
    * Map View: Displays location information as well as ability to toggle through places. 
    * Google Maps embed, both for choosing a location & displaying suggestions
    * Google Calendar sharing
* places service (HTTP service serving data from Places, etc.)
    * Google Places API;
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




## Testing

    ########
    # TODO #
    ########
