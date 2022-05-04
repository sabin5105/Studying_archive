# 1. map
# 기존 리스트를 수정해 새로운 리스트를 만들 떄 사용
# map 객체 생성
# map(myfunction, list_tuple_dictionary)
print(list(map(int,['1','2','3','4'])))

# 리스트 모든 요소의 공백 제거
items = ['  mouse   ',' keyboard   ']

# 1. for 사용
# for i in range(len(items)):
#     items[i] = items[i].strip()
# print(items)

# 2. map 사용
# def strip_all(x):
#     return x.strip()
# items = list(map(strip_all, items))
# print(items)

# 3. map + lambda 사용
items = list(map(lambda x : x.strip(), items))
print(items)


# 2. filter
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때
# list(filter(myfunction, mylist))

def func(x):
    return x<0
print(list(filter(func,[-1,-2,0,5,7])))

# 리스트에서 길이가 3이하인 문자들만 필터링
# for 사용
# animals = ['dog','monkey','cat','dragon']
# result =[]
# for animal in animals:
#     if len(animal) <= 3:
#         result.append(animal)
# print(result)

# filter 사용
# animals = ['dog','monkey','cat','dragon']
# def word_check(x):
#     return len(x) <= 3
# result = list(filter(word_check, animals))
# print(result)

# filter + lambda 사용
animals = ['dog','monkey','cat','dragon']
result = list(filter(lambda x : len(x)<=3, animals))
print(result)