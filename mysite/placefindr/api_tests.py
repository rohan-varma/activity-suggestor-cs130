import requests
import json
import random
import string



if __name__ == '__main__':
	data = {
	'location': 'UCLA',
	'radius': 5000,
	}
	print(data)
	res = requests.get('http://localhost:8000/api/suggest/', params = data)
	print(res.status_code)
	r = res.json()
	print('results are')
	actual_results = r['results']
	print(len(actual_results))
	#print(list(actual_results[0].keys()))
	example_result = actual_results[0]
	#print(list(example_result.items()))
	all_result_names = [res['name'] for res in actual_results]
	print(all_result_names)