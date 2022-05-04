class Item:
    def __init__(self,name,price,weight,isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self):
        print(f"[{self.name}] 판매 가격은 {self.price}")
    def discard(self):
        if self.isdropable == True:
            print("해당 아이템을 버렸습니다")
        elif self.isdropable == False:
            print("해당 아이템을 버릴 수 없습니다")    

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}]의 무게는 {self.weight}")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"[{self.name}]의 {self.effect} 사용")

sword = WearableItem('칼',1000,50,True,'반짝거리다')
sword.wear()
sword.sale()
sword.discard()

potion = UsableItem("물약", 15000, 0.1, False, "투명효과")
potion.discard()
potion.sale()
potion.use()
