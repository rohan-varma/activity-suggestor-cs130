
MILES_TO_METERS_CONVERSTION_CONSTANT = 1609.344

def get_types_from_request(query_dict):
    if 'types' not in query_dict:
        return []
    li = query_dict['types'].split(',')
    return [s.strip() for s in li]

def get_radius_from_request(query_dict):
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