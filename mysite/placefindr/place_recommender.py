from googleplaces import GooglePlaces, types, lang
from django.conf import settings

class PlaceRecommender(object):
    """
    Class responsible for grabbing the place recommendations.
    """

    def __init__(self):
        self.google_places = GooglePlaces(settings.GOOGLE_API_KEY)

    def get_places(self, location=None, radius=None, types=None, pagetoken=None):
        """
        Get places based on a location, radius, and a list of place types.

        :param location: String of the search location.
        :param radius: Radius from the search location (type int).
        :param types: List of type strings supported by the Google Places api
                      suported types.
        :param pagetoken: pagetoken used to get more results from a previous
                          search. Will ignore other parameters if used.
        :return: GooglePlacesSearchResult containing the search results
        """
        print('types are: {}'.format(types))
        if pagetoken:
            return self.google_places.nearby_search(pagetoken=pagetoken)
        else:
            return self.google_places.nearby_search(location=location,
                                                    radius=radius,
                                                    types=types)
