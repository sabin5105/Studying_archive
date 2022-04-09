korean = int(input("국어 >>> "))
math = int(input("수학 >>> "))
english = int(input("영어 >>> "))

average_score = (korean+math+english)/3

if korean <= 100 and math <= 100 and english <= 100:
    if average_score >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다")