
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
        return radius
    except ValueError:
        return 8000 # 5 miles