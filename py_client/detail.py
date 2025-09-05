import requests

endpoint = 'http://localhost:8000/api/products/'

get_response = requests.post(endpoint, {"title": "Hello World"})


print(get_response.json())