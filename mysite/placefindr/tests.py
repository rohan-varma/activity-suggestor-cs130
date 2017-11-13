# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .place_recommender import PlaceRecommender

class PlaceRecommenderTests(TestCase):

    def test_gets_location_results_from_location_and_token(self):
        recommender = PlaceRecommender()
        response = recommender.get_places(location="UCLA", radius=8000)
        self.assertNotEqual(response.places, [])
        next_response = recommender.get_places(pagetoken=response.next_page_token)
        self.assertNotEqual(next_response.places, [])

# Holding off on this until front end implemented. They may change these views.
class RecommenderViewTests(TestCase):

    def test_throws_404_if_no_location(self):
        pass

    def test_gets_json_from_location_and_token(self):
        pass
