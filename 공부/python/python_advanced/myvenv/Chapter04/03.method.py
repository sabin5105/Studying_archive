class Unit:
    """
    인스턴스 속성 : 이름, 체력, 방어막, 공격력
    클래스 속성 : 전체 유닛 개수
    비공개 속성
    """
    count = 0
    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.__hp = hp
        self.shield = shield
        self.damage = damage
        print(f"[{self.name}](이)가 생성 되었습니다")
        Unit.count += 1

    def __str__(self):
        return f"[{self.name}] 체력 : {self.__hp} 방어력 : {self.shield} 공격력 : {self.damage}"
        
    # 인스턴스 메서드 (instance method)
    # 인스턴스 속성에 접근할 수 있는 메서드
    def hit(self, damage):
        # 데미지 < 방어막 -> 방어막 감소
        if (damage) <= (self.shield):
            self.shield -= (damage)
            print(f"체력 : {self.__hp} 방어막 : {self.shield}")
        # 방어막 < 데미지 -> 방어막 감소 및 체력감소
        elif (self.shield) < (damage):
            self.__hp = self.__hp - (damage - self.shield)
            self.shield = 0      
            if self.__hp <= 0:
                print("유닛이 사망하였습니다")
            else:
                print(f"체력 : {self.__hp} 방어막 : {self.shield}")                  

    # 클래스 메서드
    # 클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛 개수 : {cls.count}")
    


probe = Unit("프로브",20,20,5)
zealot = Unit("질럿",100,60,16)
dragon = Unit("드라군",100,80,20)

print(zealot)
probe.hit(30)

Unit.print_count()

print(dir(probe))