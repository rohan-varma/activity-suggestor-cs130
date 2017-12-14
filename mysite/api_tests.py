import requests
import json
import random
import string

def test_basic_call():
	data = {
	'location': 'UCLA',
	'radius': 5000,
	}
	print(data)
	res = requests.get('http://localhost:8000/api/suggest/', params = data)
	assert res.status_code == 200
	res.json()
	# r = res.json()
	# actual_results = r['results']
	# all_result_names = [res['name'] for res in actual_results]
	# print(all_result_names)

def test_type_input():
	data = {
		'location': 'UCLA',
		'radius': 5000,
		'types': 'bakery, bank'
		}
	print(data)
	res = requests.get('http://localhost:8000/api/suggest/', params = data)
	assert res.status_code == 200
	print(type(res))
	# exit()
	# r = res.json()
	# actual_results = r['results']
	# all_result_names = [res['name'] for res in actual_results]
	# print(all_result_names)	


if __name__ == '__main__':
	test_basic_call()
	test_type_input()