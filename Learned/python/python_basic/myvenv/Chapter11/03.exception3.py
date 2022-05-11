class PositivieNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가")

try:
    num = int(input("음수를 입력해주세요 >>> "))
    if num >= 0:
        raise PositivieNumberError
except PositivieNumberError as e:
    print("에러발생", e)