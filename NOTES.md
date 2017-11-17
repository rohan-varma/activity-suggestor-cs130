# CS 130 Project Notes

[See this page on GitHub](https://github.com/rohan-varma/activity-suggestor-cs130/blob/master/NOTES.md)

<s>This document focuses on implementation as opposed to high level details; see the Google Doc for those</s> **The Google Doc currently contains the "main" version of the spec; however, it is deprecated in favor of this document & README.md. It's still useful for discussions and draft suggestions though. This document will eventually become the final version of the spec.**  
[Google Doc](https://docs.google.com/document/d/1ltMKhYdVDBOj4s401b5TbzwYUphTIoVpafdfUb2n-J4/) for those. 

For discussions and issues see the [issues page](https://github.com/rohan-varma/activity-suggestor-cs130/issues/).


## High level overview

Workspace structure (under /mysite)

| path | description |
| ---- | ----------- |
| `manage.py` | django management script |
| `mysite/` | django root directory (this is like a "main" (entry point) function) |
| `placefindr/` | main backend |
| `static/` | main UI + static assets |

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
| `/results?location=<...>&... | the results page showing location suggestion on Google Maps |
| `/api/suggest/?<...>` | the suggestion service; returns suggestions in JSON format |
| `/api/share/?<...>` | the sharing service; sends message containing Google Maps link to specified address <br/>no user authentication is currently enforced |
