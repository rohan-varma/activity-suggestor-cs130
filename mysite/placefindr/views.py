# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.http import Http404 # django's http status codes
from urllib.parse import parse_qsl
import json

from django.template import loader

# import .sharer
from .place_recommender import PlaceRecommender

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
        radius = get_radius_from_request(query_dict)
        types = get_types_from_request(query_dict)
        print('searching with loc {} radius {} and type {}'.format(location, radius, types))
        places = recommender.get_places(location=location,
                                       radius=radius,
                                       types=types)


    template = loader.get_template('placefindr/index.html')
    #raw_response = json.dumps(places.raw_response)
    print('RAW RESPONSE FOLLOWS')
    print(places.raw_response)
    context = {
        #'raw_response': JsonResponse(places.raw_response)
        #'raw_response': d,
        'raw_response': places.raw_response
    }

    return HttpResponse(template.render(context, request))

    # return JsonResponse(places.raw_response)
