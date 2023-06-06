import requests

URL = 'https://httpbin.org/post'

data = {
    "comments": "", 
    "custemail": "pasha@mail.com", 
    "custname": "Pasha", 
    "custtel": "13232332453", 
    "delivery": "", 
    "size": "large", 
    "topping": "bacon"
}
    
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-647f157e-0e510f1658a2f093456a750b"
}

session_1 = requests.Session() # Держит в одной сессии 

r = session_1.post(URL, headers=headers, data=data)

print(r.status_code)
print(r.text)