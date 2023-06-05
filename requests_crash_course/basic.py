import requests

print('\n------------------------------GET---------------------------------\n')

params = {
    'name': 'Dima',
    'age': 25,
}

response = requests.get('https://httpbin.org/get', params=params)
print(response.url)
print(response.status_code)

print(response.json())

print('\n------------------------------POST--------------------------------\n')

payload = {
    'name': 'Dima',
    'age': 25,
}

response = requests.post('https://httpbin.org/post', data=payload)
print(response.url)
print(response.status_code)

print(response.json())

