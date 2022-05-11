# 상속
# : 클래스들의 중복된 코드를 제거하고 유지보수를 편하기 하기 위함

# 클래스 변수
# : 인스턴스들이 모두 공유하는 변수

import random
# parents class
class Monster:
    max_num = 1000      # 클래스 변수
    def __init__(self, name, health, attack):
        self.name = name
        self.attack = attack
        self.health = health
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# child class
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):         # method override
        print(f"[{self.name}] 헤엄치기")   

class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name,health,attack)
        self.skills = ('불 뿜기','꼬리 치기','날개 치기')

    def move(self):         # method override
        print(f"[{self.name}] 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")

wolf = Wolf('울프',1500,200)
wolf.move()
print(wolf.max_num)

shark = Shark('샤크',3000,400)
shark.move()
print(shark.max_num)

dragon = Dragon('드래곤',8000,800)
dragon.move()
dragon.skill()
print(dragon.max_num)