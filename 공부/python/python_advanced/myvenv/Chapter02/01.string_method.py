# .upper()
# .lower()
# "오늘 날씨는 흐림".replace("흐림", "맑음") -> "오늘 날씨는 맑음"
# "hello world".find("world") -> 6
# "This cat is my cat".count("cat") -> 2
# .split()
# ''.join([mylist])
# .lstrip() - leftstrip .rstrip() - rightstrip .strip()

# 1. replace
# 문자열 교체
a = "오늘 날씨는 흐림 입니다".replace("흐림", "맑음")
print(a)

# 2. find
# 문자열 찾기
b = "hello world".find("world")
print(b)

# 3. split
# 문자열 분리
c = 'NIKE:270:xxx'.split(":")
print(c)

# 4. strip
# 문자열 공백 제거
d = '   Yeah    '.lstrip()
e = '   Yeah    '.rstrip()
f = '   Yeah    '.strip()
print(d,e,f)