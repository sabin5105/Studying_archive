# 함수를 사용하는 이유

# 함수를 사용하지 않는 경우
print("안녕하세요 김동준님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다")
print("안녕하세요 이사빈님")
print("현재 프리미엄 서비스 사용기간이 15일 남았습니다")


# 함수를 사용한 경우
def printMessage(name, date):
    print("안녕하세요 {} 님".format(name))
    print("현재 프리미엄 서비스 사용기간이 {}일 남았습니다".format(date))

printMessage('김동준',30)
printMessage('이사빈',15)
