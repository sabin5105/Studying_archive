from pydoc import stripid
from bs4 import BeautifulSoup as BS
import requests as req

url = 'https://finance.naver.com/marketindex/exchangeList.naver'
res = req.get(url)
soup = BS(res.text,"html.parser")

tds = soup.find_all("td")

names = []
for td in soup.select('td.tit'):
    names.append(td.get_text(strip=True))

prices = []
for td in soup.select('td.sale'):
    prices.append(td.get_text(strip=True))

print(names)
print(prices)