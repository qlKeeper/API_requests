import requests

response = requests.get("https://reqres.in/api/users?page=2")
code = response.status_code
assert code == 200, "Статус код не совпадает!"

print(response.json())
print(response.headers)