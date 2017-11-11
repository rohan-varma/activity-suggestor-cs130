# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse, Http404
from .place_recommender import PlaceRecommender

def recommender(request):
    # return HttpResponse("Hello, world. You're at the placefindr index.")
    recommender = PlaceRecommender()
    query_dict = request.GET.dict()
    if 'pagetoken' in query_dict:
        # Increment page token? query_result.next_page_token
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
    return JsonResponse(places.raw_response)
