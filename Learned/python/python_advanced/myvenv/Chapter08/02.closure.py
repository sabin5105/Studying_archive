# 1. 내부 함수
# 함수 안에 또다른 함수를 정의

def outer(name):
    def inner():
        print(name, '님 안녕하세요')
    return inner

func = outer("startcoding")
#func()

# 2. 클로저
# 함수가 종료되어도 자원을 사용할 수 있는 함수

# 조건
# 1) 내부함수
# 2) 외부 함수의 변수를 참조
# 3) 외부함수가 내부함수를 반환

def greeting(name, age, gender):
    def inner():
        print(name,'님 안녕하세요')
        print('age: ', age)
        print('gender: ', gender)
    return inner

closure = greeting('nami',27,'female')
closure()

#print(closure.__closure__[0].cell_contents)

for i in closure.__closure__:
    print(i.cell_contents)

# 전역변수를 사용해서 대체가능
# 전역변수 사용 최소화하는 것이 좋다(네이밍문제, 스코프문제)
