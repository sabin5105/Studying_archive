from operator import truediv
import threading

# 스레드에서 실행할 함수
def work():
    print("[sub]")
    keyword = input("[sub] 검색어를 입력하세요 >>> ")
    print(f"[sub] {keyword}로 검색을 시작합니다...")
    print("[sub] end")

# 메인 스레드에서 실행되는 부분
print("[main]")

worker = threading.Thread(target=work)
worker.daemon = True
worker.start()

print("[main] 메인 스레드는 자기일을 합니다...")
print("[main] end")