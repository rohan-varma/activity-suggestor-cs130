from googleplaces import GooglePlaces, types, lang

# Add documentation and testing

class PlaceRecommender:

    def __init__(self, api_key):
        self.api_key = api_key
        self.google_places = GooglePlaces(api_key)

    # Add additional processing needed for front-end. Maybe return just raw JSON?
    # Take in a places filter class instead of individual variables?
    def get_places(self, location=None, radius=None, types=None, pagetoken=None):
        return self.google_places.nearby_search(location=location,
                                                radius=radius,
                                                types=types,
                                                pagetoken=pagetoken)

# place.get_details()
# query_result.next_page_token
