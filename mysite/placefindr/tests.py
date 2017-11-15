# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
This file contains test cases for the PlaceFindr backend.
'''

from django.test import TestCase

from .place_recommender import PlaceRecommender
#from . import sharer
from .sharer import share_via_email
from . import views

class PlaceRecommenderTests(TestCase):

    def test_gets_location_results_from_location_and_token(self):
        recommender = PlaceRecommender()
        response = recommender.get_places(location="UCLA", radius=8000)
        print("response is {}".format(response))
        self.assertNotEqual(response.places, [])
        print(response.next_page_token)
        return True
        next_response = recommender.get_places(pagetoken=response.next_page_token)
        self.assertNotEqual(next_response.places, [])

class SharerValidationTests(TestCase):

    def test_email_recipient(self):
        self.assertEqual(share_via_email(None, "Nope"), 1)

    def test_email_content_placeid(self):
        pass

class SharerViewTests(TestCase):

    def setUp(self):
        pass

    def test_missing_parameters(self):
        pass

    def test_bad_sharemethod_url(self):
        pass

    def tearDown(self):
        pass

# Holding off on this until front end implemented. They may change these views.
class RecommenderViewTests(TestCase):

    def test_throws_404_if_no_location(self):
        pass

    def test_gets_json_from_location_and_token(self):
        pass
