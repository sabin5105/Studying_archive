# 상속
# : 클래스들의 중복된 코드를 제거하고 유지보수를 편하기 하기 위함

# parents class
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.attack = attack
        self.health = health
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# child class
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):         # method override
        print(f"[{self.name}] 헤엄치기")   

class Dragon(Monster):
    def move(self):         # method override
        print(f"[{self.name}] 날기")

wolf = Wolf('울프',1500,200)
wolf.move()

shark = Shark('샤크',3000,400)
shark.move()

dragon = Dragon('드래곤',8000,800)
dragon.move()