# CS 130 Project Notes

Location suggestor built for CS 130 by Elizabeth Muenchow, John Song, Aravind Sripathy, Lucas Tecot, Rohan Varma, and Henry Yang

[See this page on GitHub](https://github.com/rohan-varma/activity-suggestor-cs130/blob/master/README.md)


## Instructions

To install all the requirements, run `pip[3] install requirements.txt`.

Run `python mysite/manage.py runserver` to start server. In order to run tests, please first `cd` into the outer `mysite` directory, before running `python manage.py test`; **otherwise test discovery will fail**.


## High level overview

Workspace structure

| path | description |
| ---- | ----------- |
| `README.md` | this file |
| `requirements.txt` | list of pip package dependencies |
| `mysite/manage.py` | django management script |
| `mysite/mysite/` | django root (entry point) directory (which confusingly has the same name as the workspace root) |
| `mysite/placefindr/` | main backend <br/>`urls.py`: URL dispatch conf for backend services <br/>`views.py`: main dispatcher for backend "views" <br/>`place_recommender.py`: the location suggestor module <br/>`sharer.py`: the sharing module <br/>`settings.py`: python file loaded by the main django `settings.py`, contains backend settings and API keys |
| `mysite/placefindr/tests.py` | tests for backend |
| `mysite/static/` | main UI + static assets <br/>`splash.html`: landing page <br/> `index.html`: results page <br/>`client.js`: frontend script <br/> `styles.css`: styles |

Main areas of functionality

* main UI
    * JS geolocation [optional]
    * Google Maps embed, both for choosing a location & displaying suggestions
    * Facebook, Google Calendar sharing
    * Geocoding (might not be necessary)
* places service (JSON service serving data from Places, etc.)
    * Google Places API; Yelp API
* sharing service
    * Emailing (emails are sent from a service account)
* UI for user feed & profile [optional]
* service for user profiles [optional]


## Features & Implementation

This section describes the web interface definitions & the internals that support them.

URLs

| URL | description |
| ---- | ----------- |
| `/` | the root path, which shows the splash page, where the user is prompted for a start location & search parameters |
| `/results?<...>` | the results page showing location suggestion on Google Maps |
| `/api/suggest/?<...>` | the suggestion service; returns suggestions in JSON format |
| `/api/share/?<...>` | the sharing service; sends message containing Google Maps link to specified address <br/>no user authentication is currently enforced |


## Testing

    ########
    # TODO #
    ########
