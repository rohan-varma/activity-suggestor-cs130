"""
helpers.py provides helper functions to our recommender.
"""
MILES_TO_METERS_CONVERSTION_CONSTANT = 1609.344

def get_types_from_request(query_dict):
    """
    Get the list of types from request dict
    :param query_dict: The dictionary from the request
    :return: List of strings, which are the types
    """
    if 'types' not in query_dict:
        return []
    li = query_dict['types'].split(',')
    return [s.strip() for s in li]

def get_radius_from_request(query_dict):
    """
    Gets the radius from the request, defaulting to 8000 if it does not exit
    :param query_dict: the dict from the request
    :return: radius, type int
    """
    if 'radius' not in query_dict:
        return 8000 # 5 miles
    try:
        radius = int(query_dict['radius'])
        radius*=MILES_TO_METERS_CONVERSTION_CONSTANT      
        # the wrapper caps it to 50000        
        radius = min(50000, radius)       
        return radius
    except ValueError:
        return 8000 # 5 miles