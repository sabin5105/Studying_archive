import requests as req

# response = res
# requests = req

res = req.get("https://api.ipify.org")
print(res.status_code) # 200
print(res.text) # 211.214.140.5
print(res.request.method)
print(res.request.headers)
print(res.raw) # byte 그대로 raw 하게 받는다
