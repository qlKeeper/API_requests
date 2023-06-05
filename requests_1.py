import requests

# делаем запрос на чтение страницы https://sky.pro/media
response = requests.get('https://sky.pro/media/')
print(response.ok) # проверяем успешен ли запрос?
print(response.text) # выводим полученный ответ на экран