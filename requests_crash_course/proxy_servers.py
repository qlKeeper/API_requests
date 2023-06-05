import requests

proxies = {
    "https": "5.161.178.132:8080",
}

response = requests.get('https://httpbin.org/get', proxies=proxies)
print(response.text)

