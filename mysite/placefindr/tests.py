# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .place_recommender import PlaceRecommender

class PlaceRecommenderTests(TestCase):

    def test_gets_location_results_from_location_and_token(self):
        recommender = PlaceRecommender()
        response = recommender.get_places(location="UCLA")
        # response.places

class RecommenderViewTests(TestCase):

    def test_throws_404_if_no_location(self):
        pass

    def test_gets_json_from_location_and_token(self):
        pass
