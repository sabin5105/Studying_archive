s = '제 생일은 11월 입니다'

# arr = s.split('생일은 ')
# s = arr[1]
# print(s.split('월')[0])

bd = s.split('생일은 ')[1].split('월')[0]
print(bd)
