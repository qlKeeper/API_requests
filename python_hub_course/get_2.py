import requests

API_KEY = '7b21f1fd780dca57a472fd4ca9a2e97b'

params = {'q': 'Москва', 'appid': API_KEY, 'units': 'metric'}

r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

if r.ok:
    print(r.json(), '\n')

x = r.json()
print(x['weather'][0]['main'], x['main']['temp'])

