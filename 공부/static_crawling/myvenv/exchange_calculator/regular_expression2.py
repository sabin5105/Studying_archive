from xmlrpc.server import DocXMLRPCRequestHandler
import requests as req
import re

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
res = req.get(url)
body = res.text

# .은 줄바꿈을 포함해서 모두 검색하는 것이 아니다
# re.DOTALL을 통해 줄바꿈을 포함해 모두 검색
r =re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print("-----")
print("환율 계산기")
print("-----")
print("")

for c in captures:
    print(c[0] + " : " + c[1])

print()
usd = float(captures[0][1].replace(",", ""))
won = int(input("달러로 바꾸길 원하는 금액(원)을 입력하세요 : "))
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러 환전 되었습니다")