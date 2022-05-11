import requests as req
import json

city = "Seoul"
apikey = "c12e5205009f240c86b11a186730ac2c"
lang = "kr"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

result = req.get(api)
data = json.loads(result.text)

print(data["weather"])
print(data["main"])
