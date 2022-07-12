# list method

# 리스트 데이터 삭제
fruits = ['apple', 'orange', 'mango']
del fruits[1]
print(fruits)

# 리스트 정렬
numbers = [5,2,3,4,1]
numbers.sort()
print(numbers)

# enumerate
words = ['s','a','b','i','n']
for index, word in enumerate(words):
    print(f"인덱스 : {index} 단어 : {word}")

