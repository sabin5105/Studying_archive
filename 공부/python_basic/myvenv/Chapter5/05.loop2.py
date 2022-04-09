# while
# : 반복 횟수가 정해지지 않았을 때 사용

i = 5
while i<9:
    print(i, "번째 다짐")
    i += 1

# 무한루프
# : 조건식에 True를 넣어서 항상 반복되게 만든 것

while True:
    x = input("종료하려면 exit를 입력하세요 >>> ")
    if x == "exit":
        break
    