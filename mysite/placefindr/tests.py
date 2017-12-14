# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .place_recommender import PlaceRecommender

from .helpers import get_types_from_request, get_radius_from_request

class HelperTests(TestCase):

    def test_get_types_from_request(self):
        test_query_dict = {'location': 'West Hollywood, CA, United States', 'open': 'true', 'radius': '50', 'types': 'amusement_park,cafe,campground,casino,clothing_store,department_store,library,movie_theater,movie_rental,night_club,park,restaurant,shopping_mall,zoo'}
        types = get_types_from_request(test_query_dict)
        assert isinstance(types, list)
        assert types == test_query_dict['types'].split(',')
        del test_query_dict['types']
        assert get_types_from_request(test_query_dict) == []

    def test_get_radius_from_request(self):
        test_query_dict = {'location': 'West Hollywood, CA, United States', 'open': 'true', 'radius': '50'}
        radius = get_radius_from_request(test_query_dict)
        assert radius == 50, "radius is actually {}".format(radius)
        del test_query_dict['radius']
        radius = get_radius_from_request(test_query_dict)
        assert radius == 8000, "radius is actually {}".format(radius)

class PlaceRecommenderTests(TestCase):

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

class RecommenderViewTests(TestCase):

    def test_throws_404_if_no_location(self):
        pass

    def test_gets_json_from_location_and_token(self):
        pass
