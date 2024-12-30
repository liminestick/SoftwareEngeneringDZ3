import requests

url = "http://127.0.0.1:8000/analyze/"
data = {"text": "I love programming!"}

response = requests.post(url, json=data)
print(response.json())