class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health

# create goblin instance 
goblin = Monster(100,10,5)
# create wolf instance 
wolf = Monster(200,1,3)

goblin.decrease_health(10)
print(goblin.get_health())

# 생성자
# : instance를 만들 때 호출되는 Method

