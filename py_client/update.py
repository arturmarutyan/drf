import requests
from getpass import getpass


password = getpass()
auth_endpoint = 'http://localhost:8000/api/auth/'

auth_response = requests.post(auth_endpoint, {"username": "artur", "password": password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpoint = 'http://localhost:8000/api/products/6/update/'

    get_response = requests.put(endpoint, {"title": "Hello World", "price": 120.99}, headers=headers)


    print(get_response.json())