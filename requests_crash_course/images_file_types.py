import requests

headers = {
    "User-Agent": "Android/12.0",
    "Accept": "image/png",
}

response = requests.get('https://httpbin.org/image', headers=headers)

with open("requests_crash_course/myimage.png", 'wb') as f:
    f.write(response.content)