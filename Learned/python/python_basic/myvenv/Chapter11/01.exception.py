# 원화를 입력, 환율 입력 -> 달러값을 출력

won = input("원화금액을 입력하세요 >>> ")
dollar = input("환율을 입력하세요 >> ")

try: # 예외가 발생할 수 있는 코드
    print(int(won)/int(dollar))

except ValueError as err: # 예외가 발생했을 떄 실행되는 코드
    print("문자열 예외가 발생했습니다", err)
except ZeroDivisionError as err:
    print("나누기 0은 불가능 합니다", err)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally: # 파일 닫기 (리소스 반환)
    print("항상 실행되는 코드")
