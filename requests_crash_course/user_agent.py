import requests

headers = {
    "User-Agent": "Android/12.0"
}

response = requests.get('https://httpbin.org/user-agent', headers=headers)

print(response.text)