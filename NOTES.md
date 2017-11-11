# CS 130 Project Notes

[See this page on GitHub](https://github.com/rohan-varma/activity-suggestor-cs130/blob/master/NOTES.md)

This document focuses on implementation as opposed to high level details; see the [Google Doc](https://docs.google.com/document/d/1ltMKhYdVDBOj4s401b5TbzwYUphTIoVpafdfUb2n-J4/) for those.

For discussions and issues see the [issues page](https://github.com/rohan-varma/activity-suggestor-cs130/issues/).


## Project structure

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

Folder structure

| path | description |
| ---- | ----------- |
| `manage.py` | management script |
| `mysite/` | django root directory (this is like a "main" (entry point) function) |
| `mysite/static/`, <br />`mysite/templates/` | main UI + shared assets |
| `apps/` | "apps" (subcomponents) |
| `apps/.../static/`, <br />`apps/.../templates/` | app-specific assets |
| `apps/suggestor/` | the main location suggestor backend |
| `apps/profiles/` | (optional) user profile handling (user "feed", account settings, etc.) |


## Implementation details

This section describes the web interface definitions & the internals that support them.


### client UI

These would be accessed directly from the root domain (e.g. `https://mysite/`).

| url | description |
| --- | ----------- |
| `/` (default landing) | Splash page (prompts user to enter a location and then preferences) |
| `/results?location=<...>&...` | Results page |

*It seems like a good idea to have a separate URL with query strings for the results page, since otherwise it would be impossible to, say, bookmark the results page (instead of having to enter your location, like, every single time). These would be handled by the client javascript. -John*


### places service

URLs for accessing the places backend should look like `https://mysite/api/suggest?location=<lat>,<long>&category=<...>&...`

... returns JSON containing a list of suggested places


*Q: How does the randomization algorithm work?*

Google Places returns locations ranked either by prominence or by proximity, which probably means we also have to 

(Also Google has a 1000 queries/day limit for the free account.)

<s>Is this scalable?</s> (Who cares? loly)

Also: yelp for reviews??


### sharing service???

As for sharing...

(we might need to consider the possibility of people using this for spamming)

<s>Security?</s> (security be damned we ain't got no time to worry about that people)
