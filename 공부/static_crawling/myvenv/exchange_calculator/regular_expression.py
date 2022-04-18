import re
# regular expression

# () : 캡쳐
# [] : 이 중 아무거나
# . : 아무거나
# * : 0개 이상
# + : 1개 이상
# ? : 없을 수도
# \ : 위 특수 기호 무효화 (메타기호)

# s = 'color'
# print(re.match(r'colou?r', s))

s = '이 영화는 A등급 입니다'
print(re.match(r'이 영화는 [ABCF]등급 입니다', s))
print(s.split('이 영화는 ')[1].split('등급')[0])
print(re.findall(r'이 (..)는 ([ABCD])등급 입니다', s))
