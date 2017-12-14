# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .place_recommender import PlaceRecommender

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
