# s = 'apple'

# print(s.find('e'))

# arr = s.split('p')
# print(arr)

s = '제 생일은 11월 입니다'
pos = s.find('생일은 ')
pos += 4
print(s[pos:pos+3])