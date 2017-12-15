"""
tests tests all of our code
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .place_recommender import PlaceRecommender

from .helpers import get_types_from_request, get_radius_from_request
import requests
import json
import random
import string

class APITests(TestCase):
    """
    APITests are our integration tests for our backend APIs
    """
    def test_basic_call(self):
        """
        test_basic_call tests a call with location and radius parameters, but no place types.
        """
        data = {
        'location': 'UCLA',
        'radius': 5000,
        }
        print(data)
        res = requests.get('http://localhost:8000/api/suggest/', params = data)
        assert res.status_code == 200

def test_type_input(self):
    """
    test_type_input tests a call with location, types, and radius parameters
    """
    data = {
        'location': 'UCLA',
        'radius': 5000,
        'types': 'bakery, bank'
        }
    print(data)
    res = requests.get('http://localhost:8000/api/suggest/', params = data)
    assert res.status_code == 200

def test_convert_radius(TestCase):
    """
    test_convert_radius tests that a radius can be converted, even if it is over capacity
    """
    data = {
        'location': 'UCLA',
        'radius': '999999999',
        'types': 'bakery, bank'
            }
    res = requests.get('http://localhost:8000/api/suggest/', params = data)
    assert res.status_code == 200    

def test_fail_loc(TestCase):
    """
    test_fail_loc tests that the call fails if no location is provided
    """
    data = {
        'location': 'UCLA',
        'radius': 5000,
        'types': 'bakery, bank'
        }
    del data[location]
    res = requests.get('http://localhost:8000/api/suggest/', params = data)
    assert res.status_code != 200


class HelperTests(TestCase):
    """
    HelperTests tests our helper functions
    """
    def test_get_types_from_request(self):
        """
        test_get_types_from_request tests that we can extract a list of types from a request
        """
        test_query_dict = {'location': 'West Hollywood, CA, United States', 'open': 'true', 'radius': '50', 'types': 'amusement_park,cafe,campground,casino,clothing_store,department_store,library,movie_theater,movie_rental,night_club,park,restaurant,shopping_mall,zoo'}
        types = get_types_from_request(test_query_dict)
        assert isinstance(types, list)
        assert types == test_query_dict['types'].split(',')
        del test_query_dict['types']
        assert get_types_from_request(test_query_dict) == []

    def test_get_radius_from_request(self):
        """
        test_get_radius_from_request tests if we can get the radius from a request
        """
        test_query_dict = {'location': 'West Hollywood, CA, United States', 'open': 'true', 'radius': '10'}
        radius = get_radius_from_request(test_query_dict)
        assert radius == 10*1609.344, "radius is actually {}".format(radius)
        del test_query_dict['radius']
        radius = get_radius_from_request(test_query_dict)
        assert radius == 8000, "radius is actually {}".format(radius)

    def test_radius_cap(self):
        """
        test_radius_cap tests that if the radius provided is over capacity, we cap it at 50,000m
        """
        test_query_dict = {'location': 'West Hollywood, CA, United States', 'open': 'true', 'radius': '50'}
        radius = get_radius_from_request(test_query_dict)
        assert radius == 50000, "radius is actually {}".format(radius)
        del test_query_dict['radius']
        radius = get_radius_from_request(test_query_dict)
        assert radius == 8000, "radius is actually {}".format(radius)

class PlaceRecommenderTests(TestCase):
    """
    PlaceRecommenderTests enumerates test cases for our place recommender
    """
    def test_gets_location_results_from_location_and_token(self):
        recommender = PlaceRecommender()
        response = recommender.get_places(location="UCLA West Hollywood, CA, United States", radius = int('8000'), types = ['amusement_park', 'bowling_alley', 'cafe', 'campground', 'movie_theater', 'night_club', 'park', 'restaurant', 'shopping_mall', 'zoo'])
        results = response.raw_response['results']
        places = response.places
        assert len(results) == len(places)

    def test_failure_call(self):
        recommender = PlaceRecommender()
        try:
            response = recommender.get_places(location="UCLA West Hollywood, CA, United States", radius = '8000', types = ['amusement_park', 'bowling_alley', 'cafe', 'campground', 'movie_theater', 'night_club', 'park', 'restaurant', 'shopping_mall', 'zoo'])
            assert 1 == 2 # we should fail before we get here
        except TypeError:
            pass # we should err when radius wasn't parse

    def test_no_location_failure(self):
        recommender = PlaceRecommender()
        try:
            response = recommender.get_places(radius = '8000', types = ['amusement_park', 'bowling_alley', 'cafe', 'campground', 'movie_theater', 'night_club', 'park', 'restaurant', 'shopping_mall', 'zoo'])
            assert 1 == 2 # we should fail before we get here
        except ValueError:
            pass # we should err when no loc is specified

### Example of a mutation test, if you take out line 25 in place_recommender.py then this test will break
    def test_radius_empty(self):
        # if the user did not specify any radius, a sensible default option should be used, and it should not error out
        recommender = PlaceRecommender()
        response = recommender.get_places(location="UCLA West Hollywood, CA, United States", types = ['amusement_park', 'bowling_alley', 'cafe', 'campground', 'movie_theater', 'night_club', 'park', 'restaurant', 'shopping_mall', 'zoo'])
        results = response.raw_response['results']
        places = response.places
        assert len(results) == len(places)

    def test_types_empty(self):
        # all types should be returned if the user did not specify any types
        recommender = PlaceRecommender()
        response = recommender.get_places(location="UCLA West Hollywood, CA, United States", radius = int('8000'))
        results = response.raw_response['results']
        places = response.places
        assert len(results) == len(places)
