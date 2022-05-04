import requests 

# get : 요청, 값 가져오는 역할
# post : 생성, 액션
# put : 수정, 덮어씌우기
# delete : 삭제
res = requests.get('https://www.naver.com')
print(res.text)