# 데코레이터
# 함수의 앞, 뒤로 부가적인 기능을 넣어주고 싶을 떄 사용
# 로깅, 권한확인

def logger(func):
    def wrapper(arg):
        print("함수시작")
        func(arg)
        print("함수끝")
    return wrapper

@logger
def print_hello(name):
    print("HELLO", name)
@logger
def print_bye(name):
    print('BYE', name)

print_hello('startcoding')
print_bye('fastcampus')
