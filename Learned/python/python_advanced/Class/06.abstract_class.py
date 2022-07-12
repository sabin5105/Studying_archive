from abc import *

class Item(metaclass=ABCMeta):
    """
    속성 : 이름
    메서드 : 줍기, 버리기
    """

    def __init__(self, name):
        self.name = name
    
    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다!")
    
    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다!")

    @abstractmethod
    def use(self):
        pass

class weapon(Item):
    """
    속성 : 공격력
    메서드 : 공격하기
    """
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
    
    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.damage}로 공격합니다!")
    
class HealingItem(Item):
    """
    속성 : 회복량
    메서드 : 사용하기
    """
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def use(self):
        print(f"[{self.name}]을(를) 사용해 {self.recovery_amount}만큼 회복합니다")

m16 = weapon("m16",110)
bandid = HealingItem("붕대",20)

m16.use()
bandid.use()