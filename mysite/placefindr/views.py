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
    return HttpResponse("Hello, world. You're at the placefindr index.")
#     # return JsonResponse()

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

def suggest(request):
    """
    Generates a JSON HttpResponse for a reqest for nearby places.
    """
    recommender = PlaceRecommender()
    query_dict = request.GET.dict()
    if 'pagetoken' in query_dict:
        pagetoken = query_dict['pagetoken']
        places = recommender.get_places(pagetoken=pagetoken)
    else:
        if 'location' not in query_dict:
            raise Http404('No location input.')
        location = query_dict['location']
        radius = query_dict['radius'] if 'radius' in query_dict else 8000  # 5 Miles
        types = query_dict['types'] if 'types' in query_dict else []
        places = recommender.get_places(location=location,
                                       radius=radius,
                                       types=types)


    template = loader.get_template('placefindr/index.html')

    context = {
        'status': places.raw_response["status"],
        'results': places.raw_response["results"],
        'next_page_token': places.raw_response["next_page_token"],
    }
    return HttpResponse(template.render({}, request))
    # return JsonResponse(places.raw_response)
