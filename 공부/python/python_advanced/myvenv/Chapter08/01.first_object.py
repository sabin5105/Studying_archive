# 일급객체?
# 1. 데이터처럼 사용 가능
# 2. 매개변수에 넘겨줄 수 있음
# 3. 리턴값으로 사용 가능

# 1. 데이터처럼 사용 가능
# 1) 함수를 변수에 할당 가능

def func(x,y):
    return x+y

add = func
print(add(1,2))

# 2) 리스트,튜플,딕셔너리에 할당 가능
def mul(x,y):
    return x*y

def div(x,y):
    return x/y

calculator = [mul,div]
print(calculator[0](5,6))

# 2. 매개변수에 넘겨줄 수 있음
def inputData():
    data = input("데이터 입력 >>> ")
    return data

def start(func):
    print("입력한 데이터는",func())

start(inputData)

# 3. 리턴값으로 사용될 수 있다
def plusTen(a):
    return a+10

def func(x):
    return plusTen(x)

print(func(5))