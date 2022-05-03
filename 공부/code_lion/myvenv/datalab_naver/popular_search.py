from bs4 import BeautifulSoup
import requests as req

url = "https://datalab.naver.com/"
res = req.get(url)
soup = BeautifulSoup(res.text,"html.parser")

nums = []
titles = []

for lis in soup.select("li.list"):
    if len(lis.select("em.num")) == 0 or len(lis.select("span.title")) == 0:
        continue
    
    nums.append(lis.select("em.num")[0].get_text(strip=True))
    titles.append(lis.select("span.title")[0].get_text(strip=True))

index_cnt = 0

for date in soup.select("span.title_cell"):
    if len(date.get_text(strip=True)) == 0:
        continue
    print(date.get_text(strip=True))
    for i in range(10):
        print(f"{nums[i+index_cnt]}. {titles[i+index_cnt]}")

    index_cnt += 10
    print("---------------------")