from selectors import SelectSelector


while True:
    print("메뉴를 입력하세요")
    select = int(input("1. 게임시작 2. 랭킹보기 3. 게임종료 >> "))

    if select == 1:
        print("게임을 시작합니다")
    elif select == 2:
        print("실시간 랭킹")
    elif select == 3:
        print("게임을 종료합니다")
        break
    else:
        print("다시 입력해주세요")