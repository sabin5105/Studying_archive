
# 기본형
# 1. 정의
def printHello():
    print("Hello")

# 2. 호출
printHello()

# 매개변수가 있는 함수 (parameter)
def sum(a,b):
    print(a+b)

sum(1,2)

# 반환값이 있는 함수
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())

# 매개변수와 반환값이 있는 함수

def add(a,b):
    result = a+b
    return result

print(add(3,4))