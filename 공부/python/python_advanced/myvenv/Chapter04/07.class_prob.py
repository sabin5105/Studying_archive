unit_info = {
    "probe": {
        "name" : "프로브",
        "mineral" : 50,
        "gas" : 0,
        "hp" : 20,
        "shield" : 20,
        "demage" : 5
    },
    "zealot": {
        "name" : "질럿",
        "mineral" : 50,
        "gas" : 0,
        "hp" : 20,
        "shield" : 20,
        "demage" : 5
    },
    "dragon": {
        "name" : "드라군",
        "mineral" : 50,
        "gas" : 100,
        "hp" : 20,
        "shield" : 20,
        "demage" : 5
    }
}

class Unit:
    def __init__(self, name, mineral, gas, hp, shield, demage):
        self.name = name
        self.mineral = mineral
        self.gas = gas
        self.hp = hp
        self.shield = shield
        self.demage = demage
    
class Player: 
    def __init__(self, nickname, mineral, gas, unitlist = []):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unitlist = unitlist

    def produce(self, name, mineral, gas, hp, shield, demage):
        if self.mineral < mineral:
           print("미네랄이 부족합니다")
        elif self.gas < gas:
            print("가스가 부족합니다")
        else:
            self.mineral -= mineral
            self.gas -= gas
            unit = Unit(name,mineral,gas,hp,shield,demage)
            self.unitlist.append(unit)
            print(f"[{name}]을 생성합니다")

player1 = Player('bisu',400,10)

player1.produce(unit_info['probe']['name'], unit_info['probe']['mineral'],unit_info['probe']['gas'],unit_info['probe']['hp'],unit_info['probe']['shield'],unit_info['probe']['demage'])
player1.produce(unit_info['zealot']['name'], unit_info['zealot']['mineral'],unit_info['zealot']['gas'],unit_info['zealot']['hp'],unit_info['zealot']['shield'],unit_info['zealot']['demage'])
player1.produce(unit_info['dragon']['name'], unit_info['dragon']['mineral'],unit_info['dragon']['gas'],unit_info['dragon']['hp'],unit_info['dragon']['shield'],unit_info['dragon']['demage'])
