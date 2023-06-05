import requests

# You can create your own requests
URL: str
r = requests.request("CREATE", URL)

print(r.headers)