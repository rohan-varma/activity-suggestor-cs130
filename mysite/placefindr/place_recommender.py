from googleplaces import GooglePlaces, types, lang
from django.conf import settings

class PlaceRecommender:

    def __init__(self):
        self.google_places = GooglePlaces(settings.GOOGLE_API_KEY)

    def get_places(self, location=None, radius=None, types=None, pagetoken=None):
        return self.google_places.nearby_search(location=location,
                                                radius=radius,
                                                types=types,
                                                pagetoken=pagetoken)

# place.get_details()
# query_result.next_page_token
