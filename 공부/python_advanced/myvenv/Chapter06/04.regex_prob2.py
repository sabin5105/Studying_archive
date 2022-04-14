datas = [
    'startcoding@naver.com',
    'start-coding@naver.com',
    'start_coding@naver.kr',
    'startcoding@k-mail.com',
    '@naver.com',
    'startcoding?@naver.com',
    'startcoding@k-mail',
    'startcoding@naver'
]

regex = re.compile('^[\w-]+@[\w-]+\.[\w.]+$')
import re

for data in datas:
    matchOBJ = re.match(regex,data)
    result = (lambda x : True if x != None else False) (matchOBJ)
    print(f'{data} {result}')