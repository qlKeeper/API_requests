import requests

params = {
    "q": "funny cats"
}

response = requests.get('https://www.google.ru/search', params=params)

print(response.status_code) # Статус код ответа
print(response.headers) # Заголовок ответа со служебной информацией
# print(response.content) # Тело ответа в байтах
print(response.text) # Тело ответа в виде текста
