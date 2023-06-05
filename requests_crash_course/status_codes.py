import requests

response = requests.get('https://httpbin.org/status/404')


if response.status_code == requests.codes.not_found:
    print("404: Not Found")
else:
    print(response.status_code)