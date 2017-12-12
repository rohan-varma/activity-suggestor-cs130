# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.http import Http404 # django's http status codes
from urllib.parse import parse_qsl
from django.views.decorators.csrf import csrf_exempt
import json
import decimal
from . import sharer
from .place_recommender import PlaceRecommender

# remove these if not using templates
from django.template import loader

def share(request, sharing_method):
    print('in share method')
    if sharing_method == 'email':
        sh = sharer.share_via_email
    elif sharing_method == 'text':
        sh = sharer.share_via_text
    else:
        return HttpResponseBadRequest('HTTP 400 - bad request\nUnknown sharing_method')

    params = parse_qsl(request.META['QUERY_STRING'])
    # user is supplied in the query string & details in json body? Or maybe make everything come from the json?
    #body = json.loads(request.body)
    try:
        if sh(params['addr'], params['placeid']) == 0:
        #if sh(params['addr'], body) == 0:
            return HttpResponseServerError('HTTP 500 - internal server error')
        else:
            return HttpResponse('HTTP 200 - OK')
    except:
        return HttpResponseBadRequest('HTTP 400 - bad request\nMissing query parameters')

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

@csrf_exempt
def suggest(request):
    """
    Generates a JSON HttpResponse for a reqest for nearby places.
    """
    query_dict = request.GET.dict()

    recommender = PlaceRecommender()
    if 'pagetoken' in query_dict:
        pagetoken = query_dict['pagetoken']
        places = recommender.get_places(pagetoken=pagetoken)
    else:
        if 'location' not in query_dict:
            raise Http404('No location input.')
        location = query_dict['location']
        radius = int(query_dict['radius']) if 'radius' in query_dict else 8000  # 5 Miles
        types = query_dict['types'].split(',') if 'types' in query_dict else []
        places = recommender.get_places(location=location,
                                       radius=radius,
                                       types=types)
    raw_response = json.dumps(places.raw_response, default=decimal_default)

    return JsonResponse(places.raw_response)
