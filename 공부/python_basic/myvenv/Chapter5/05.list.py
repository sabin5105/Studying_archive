# list
# 데이터 추가 - mylist.append(data)
# 데이터 할당 - mylist[index] = data
# 데이터 삭제 - del mylist[index]
# 슬라이싱(slicing) - mylist[begin_index : end_index+1]
#   - 반환하고자 하는 길이만큼 설정 후 반환
# 리스트 길이 - len(mylist)
# 리스트 정렬 - mylist.sort()

# 데이터가 있는 리스트
animals = ['가물치','메뚜기','비단뱀','사빈']

# 데이터가 없는 리스트
empty = []

# 데이터 접근
print(animals[2])
print(animals[-1]) # 마지막 데이터 반환

# 데이터 추가
animals.append('고라니')
print(animals)

# 데이터 할당
animals[1] = '청개구리'
print(animals)

# 데이터 삭제
del animals[0]
print(animals)

# 슬라이싱
print(animals[1:3])
print(animals[:]) # 전체 출력
print(animals[:3])
print(animals[1:])

# 리스트 길이
print(len(animals))

# 리스트 정렬
animals.sort(reverse=True)
print(animals)