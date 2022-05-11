from bs4 import BeautifulSoup
import requests as req

url = "https://search.shopping.naver.com/search/all?query=%EB%A7%A5%EB%B6%81+%EC%BC%80%EC%9D%B4%EC%8A%A4&cat_id=&frm=NVSHATC"
res = req.get(url)
soup = BeautifulSoup(res.text,"html.parser")

arr = soup.select("ul.list_basis div>a:first-child[title]")
print(arr)
for a in arr:
    print(a.get_text(strip=True))