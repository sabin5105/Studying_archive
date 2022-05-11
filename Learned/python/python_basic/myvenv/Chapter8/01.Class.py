# 클래스를 사용하는 이유
champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print("{}님 소환사의 협곡에 오신 것을 환영합니다".format(champion1_name))

champion2_name = "리신"
champion2_health = 800
champion2_attack = 95

print("{}님 소환사의 협곡에 오신 것을 환영합니다".format(champion2_name))

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)

print("=========== 클래스를 사용하는 경우 ===========")

class Champions:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신 것을 환영합니다.")
    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack}")

ezreal = Champions('이즈리얼',800, 90)
leesin = Champions('리신', 900, 95)

ezreal.basic_attack()
leesin.basic_attack()