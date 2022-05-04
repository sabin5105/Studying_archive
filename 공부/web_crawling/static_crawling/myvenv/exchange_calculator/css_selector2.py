from bs4 import BeautifulSoup
import requests as req

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
res = req.get(url, headers={
    "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
})
# User-agent 헤더로 넣는 이유 - 내 정보를 request에 함께 보냄

soup = BeautifulSoup(res.text,"html.parser")

# list comprehension
# [a for a in range(5)]

# for a in arr:
#   print(a.get_text(strip=True))

# arr = [a.get_text(strip=True) for a in soup.select("div.name")]
# print(arr)

for description in soup.select("div.descriptions-inner"):
    ads = description.select("span.ad-badge")
    if len(ads) > 0:
        print("광!!!고!!!!")
    print(description.select("div.name")[0].get_text(strip=True))
        