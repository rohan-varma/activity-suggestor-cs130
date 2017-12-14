# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.http import Http404 # django's http status codes
from urllib.parse import parse_qsl
import json
import urllib   
from .models import RecommendedPlace

from django.template import loader

# import .sharer
from .place_recommender import PlaceRecommender

MILES_TO_METERS_CONVERSTION_CONSTANT = 1609.344
# Create your views here.

def index(request):
    template = loader.get_template('placefindr/splash.html')
    return HttpResponse(template.render({}, request))

def share(request, sharing_method):
    if sharing_method == 'email':
        sh = share_via_email
    elif sharing_method == 'text':
        sh = share_via_text
    else:
        return HttpResponseBadRequest('Unknown sharing_method parameter')

    # user is supplied in the query string & details in json body? Or maybe make everything come from the json?
    params = parse_qsl(request.META['QUERY_STRING'])
    #body = json.loads(request.body)
    try:
        if sh(params['addr'], params['placeid']) == 0:
        #if sh(params['addr'], body) == 0:
            return HttpResponseServerError('')
        else:
            return HttpResponse('')
    except:
        return HttpResponseBadRequest('')


def get_types_from_request(query_dict):
    if 'types' not in query_dict:
        return []
    li = query_dict['types'].split(',')
    return [s.strip() for s in li]

def get_radius_from_request(query_dict):
    if 'radius' not in query_dict:
        return 8000 # 5 miles
    try:
        radius = int(query_dict['radius'])
        return radius
    except ValueError:
        return 8000 # 5 miles

def get_radius(query_dict):
    if 'radius' not in query_dict:
        return 8000 # 5 miles
    try:
        radius = int(query_dict['radius'])
        # convert it to meters
        radius*=MILES_TO_METERS_CONVERSTION_CONSTANT
        # the wrapper caps it to 50000
        radius = min(50000, radius)
        return radius
    except ValueError:
        return 8000

def suggest(request):
    """
    Generates a JSON HttpResponse for a reqest for nearby places.
    """
    print("in suggest")
    recommender = PlaceRecommender()
    query_dict = request.GET.dict()
    print("query dict is {}".format(query_dict))
    if 'pagetoken' in query_dict:
        pagetoken = query_dict['pagetoken']
        places = recommender.get_places(pagetoken=pagetoken)
    else:
        if 'location' not in query_dict:
            raise Http404('No location input.')
        location = query_dict['location']
        radius = get_radius(query_dict)
        types = get_types_from_request(query_dict)
        print('searching with loc {} radius {} and type {}'.format(location, radius, types))
        places_result = recommender.get_places(location=location,
                                       radius=radius,
                                       types=types)


    template = loader.get_template('placefindr/index.html')
    #raw_response = json.dumps(places.raw_response)
    # the important things are places_result.raw_response and places_result.places
    assert len(places_result.places) == len(places_result.raw_response['results']), "houston we have a problem"
    # rm hotel
    hotel = ['inn', 'motel', 'hotel']
    not_a_hotel = lambda s: hotel[0] not in s.lower() and hotel[1] not in s.lower() and hotel[2] not in s.lower()
    google_places = [place for place in places_result.places if not_a_hotel(place.name)]
    places_result.raw_response['results'] = [place for place in places_result.raw_response['results'] if not_a_hotel(place['name'])]
    for p1, p2 in zip(google_places, places_result.raw_response['results']):
        print(p1.name)
        print(p2['name'])

    google_places = google_places[:15 if 15 < len(places_result.places) else len(google_places)]
    places_result.raw_response['results'] = places_result.raw_response['results'][:15 if 15 < len(places_result.raw_response['results']) else len(places_result.raw_response['results'])]
    assert len(google_places) <= 15, "houston we have a problem"
    assert len(places_result.raw_response['results']) <= 15, "houston we have a problem"
    name_to_place = {}
    ### MAKE IT 15
    if not google_places:
        print('WARNING: No places returned!')
    for place in google_places:
        place.get_details()
        name_to_place[place.details['name']] = place
    for place in places_result.raw_response['results']:
        addr = name_to_place[place['name']].formatted_address
        rating = name_to_place[place['name']].rating
        phone = name_to_place[place['name']].local_phone_number
        place['formatted_address'] = addr
        place['rating'] = rating
        place['phone'] = phone


    example_place = google_places[len(google_places)-1] if google_places else None
    if example_place:
        example_place.get_details() # makes another api call
    rp = RecommendedPlace(place_name = 'Place1', place_ranking = 5, num_times_shared = 0)
    rp.save()   
    #places_result.raw_response['results'] is a list where each element is a dict describing the place
    # match on that
    context = {
        #'raw_response': JsonResponse(places.raw_response)
        #'raw_response': d,
        'raw_response': places_result.raw_response
    }

    return HttpResponse(template.render(context, request))

    # return JsonResponse(places.raw_response)
