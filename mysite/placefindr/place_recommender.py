from googleplaces import GooglePlaces, types, lang
from .settings import settings

class PlaceRecommender:
    """
    Class responsible for grabbing the place recommendations.
    """

    def __init__(self):
        self.google_places = GooglePlaces(settings.GOOGLE_API_KEY)

    def get_places(self, location=None, radius=None, types=None, pagetoken=None):
        """
        Get places based on a location, radius, and a list of place types.

        :param location: String of the search location.
        :param radius: Radius from the search location.
        :param types: List of type strings supported by the Google Places api
                      suported types.
        :param pagetoken: pagetoken used to get more results from a previous
                          search. Will ignore other parameters if used.
        :return: GooglePlacesSearchResult containing the search results
        """
        if not location:
            raise ValueError("You should specify a location")
        else:
            print('locations are {} {} {} {}'.format(location, radius, types, pagetoken))
            radius = 8000 if radius is None else radius # rm this line for a mutation
            return self.google_places.nearby_search(location=location,
                                                    radius=radius,
                                                    types=types,
                                                    pagetoken=pagetoken)
