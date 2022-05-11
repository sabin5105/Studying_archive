"""
image Post 할 때 http protocol

Form Data e.g.)
------WebKitFormBoundary7DHzqJhO2wUGkAqT
Content-Disposition: form-data; name="image"; filename="62D8C52B-0F69-4540-A310-7EB930402637_1_105_c.jpeg"
Content-Type: image/jpeg


------WebKitFormBoundary7DHzqJhO2wUGkAqT
Content-Disposition: form-data; name="type"

file
------WebKitFormBoundary7DHzqJhO2wUGkAqT
Content-Disposition: form-data; name="name"

62D8C52B-0F69-4540-A310-7EB930402637_1_105_c.jpeg
------WebKitFormBoundary7DHzqJhO2wUGkAqT--
"""

import requests as req

url = "https://api.imgur.com/3/image?client_id=546c25a59c58ad7"

# f = open("./macmiller.jpg", "rb")
# img = f.read()

with open("./macmiller.jpg", "rb") as f:
    img = f.read()
f.close()

res = req.post(url, files={
    "image" : img,
    "type" : "file",
    "name" : "macmiller.jpg"
})
print(res.status_code)
print(res.text)
# status_code 
# 200 : 성공
# 400 : 보내는 사람 잘못 (client)
# 500 : 받는 사람 잘못
link = res.json()["data"]["link"]
print(link)

