# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from urllib.parse import parse_qsl
import json

import sharer

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the placefindr index.")
    # return JsonResponse()

def suggest(request):


def share(request, sharing_method):
    '''
    '''
    if sharing_method == 'email':
        sh = share_via_email
    else if sharing_method == 'text':
        sh = share_via_text
    else:
        return HttpResponseBadRequest('Unknown sharing_method parameter')

    # user is supplied in the query string & details in json body? Or maybe make everything come from the json?
    params = parse_qsl(request.META['QUERY_STRING'])
    #body = json.loads(request.body)
    try
        if sh(params['addr'], params['placeid']) == 0:
        #if sh(params['addr'], body) == 0:
            return HttpResponseServerError('')
        else:
            return HttpResponse('')
    except
        return HttpResponseBadRequest('')

