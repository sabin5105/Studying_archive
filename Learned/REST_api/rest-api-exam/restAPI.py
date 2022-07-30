import requests
import json

url_items = "http://localhost:3000/todos/"
newItem = {
    "id": 4,
    "content": "Python",
    "completed": True
    }
response = requests.post(url_items, data=newItem)

print(response.text)
print(response.json()["content"])
