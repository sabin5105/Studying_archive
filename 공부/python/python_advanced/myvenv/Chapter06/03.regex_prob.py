import re

dates = ['2022/08/08',
'1000/01/01',
'9999/12/31',
'900/02/02',
'12000/10/26',
'2021/13/01',
'2023/2/02',
'2024/06/3',
'2023/06/35'
]

regex = '^\d{4}\/(0[0-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[0-1])$'

for date in dates:
    matchOBJ = re.match(regex,date)
    result = (lambda x : True if x != None else False)(matchOBJ)
    print(f'{date} {result}')