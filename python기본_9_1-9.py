# #**9-1 클래스(어렵지만 python에서 굉장히 중요한 부분!)
# # 비유를 하자면, '붕어빵 틀'이라고 생각하면 됨(그 틀에 재료를 넣으면 틀은 1개인데 붕어빵은 무한대로 만들 수 있음)
# # 일반적인 설명으로는, 서로 연관이 있는 변수와 함수의 집합정도로 이해하면 될 것 같음
# class Unit: 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 50, 5)
# tank = Unit("탱크", 150, 35)

# #**9-2 __init__(파이썬에서 쓰이는 생성자 즉, 마린이나 탱크같은 객체가 만들어질 때 자동으로 호출되는 부분)
# # 마린과 탱크는 Unit 클래스의 인스턴스라고 표현함 
# # 객체(마린, 탱크같은)가 생성될 때에는 기본적으로 __init__함수에 정의된 갯수와 동일하게 해야 함(self 제외하고)
# # 예를 들어, tank2 = Unit("탱크2", 120) 이렇게만 넣을 경우 오류 발생 

# #**9-3 멤버변수 
# # 클래스 내에서 정의된 변수, 그 변수를 가지고 외부에서 실제로 쓸 수 있는 것 ex)self.name, self.hp 이런 변수
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 멤버변수를 외부에서 wraith1.name 이렇게 쓸 수 있음 
# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)_스타크래프트 설명
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 클래스 외부에서 clocking이라는 변수를 추가로 할당한 것(파이썬은 어떤 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있음)
# if wraith2.clocking == True: # 외부에서 추가 할당한 변수는 그 할당을 한 객체에서만 적용됨!(ex-wraith1에서는 clocking을 할당하지 않은 채로 쓰면 오류남)
#     print("{0} 는 현재 클로킹 상태입니다. ".format(wraith2.name))

# #**9-4 메소드 (클래스에서 멤버변수 이외의 함수들)
# class AttackUnit: 
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}"\
#             .format(self.name, location, self.damage)) #self.name, self.damage같은 'self.~~' 변수는 클래스 자기자신에 있는 멤버변수의 값을 출력, location은 그냥 전닯받은 값을 출력
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
# firebat1 = AttackUnit("파이어뱃", 50, 16) # 파이어뱃 : 공격유닛, 화염방사기_스타크래프트 설명
# firebat1.attack("5시")
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# #**9-5 상속(상속받는 유닛의 멤버변수와 메소드를 그대로 사용할 수 있게 됨) 
# # 일반유닛
# # class Unit: 
# #     def __init__(self, name, hp):
# #         self.name = name
# #         self.hp = hp
# # 공격유닛
# # class AttackUnit(Unit): # 상속받고 싶은 클래스를 ()괄호 안에 넣어줌 (AttackUnit클래스가 Unit클래스를 상속받음_AttackUnit클래스:자식/Unit크랠스:부모)
# #     def __init__(self, name, hp, damage):
# #         Unit.__init__(self, name, hp) # 상속받는 클래스의 멤버변수 가져올 때 (Unit에서 만들어진 생성자를 호출)
# #         self.damage = damage

# #**9-6 다중상속
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
# # 공중공격유닛_다중상속 예시
# class FlyableAttackUnit(AttackUnit, Flyable): # 이 클래스는 두 개의 클래스를 상속받아 초기화해준 것뿐임(두 클래스의 멤버변수, 메소드 다 받음)
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) # 발키리 : 공중공격유닛, 한번에 14발 미사일 발사_스타크래프트 설명
# valkyrie.fly(valkyrie.name, "3시")

# #**9-7 메소드 오버라이딩
# # -> 부모클래스에서 정의한 메소드말고 자식클래스에서 정의한 메소드를 쓰고 싶을 때 메소드를 새롭게 정의해서 사용하는 것
# class Unit: 
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit): 
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage)) 
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# class FlyableAttackUnit(AttackUnit, Flyable): 
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0으로 처리
#         Flyable.__init__(self, flying_speed)
#     def move(self, location): # move 재정의 (메소드 오버라이딩)_상속받고 있는 AttackUnit의 move함수(Unit에게 상속받은)를 쓰지 않고 다시 재정의해서 씀
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
 
# vulture = AttackUnit("벌쳐", 80, 10, 20) # 벌쳐 : 지상유닛, 기동성이 좋음_스타크래프트 설명 
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3) # 배틀크루저 : 공중유닛, 체력과 공격력 굉장히 좋음_스타크래프트 설명
# # 아래와 같이, 벌쳐와 배틀크루저가 지상유닛인지 공격유닛인지 항상 확인해가면서 함수(move/fly)를 구별해서 써줘야 함;; 되게 귀찮음..  
# vulture.move("11시") 
# # battlecruiser.fly(battlecruiser.name,"9시")
# # 그러므로, '메소드 오버라이딩'을 써서 똑같이 move함수만 쓰면 지상유닛인 경우에는 이동을 하고, 공중유닛인 경우에는 날아갈 수 있도록 처리하겠음
# battlecruiser.move("9시") 

# #**9-8 pass (아무것도 안하고 그냥 넘어가는 의미, 정의O, 오류X)
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, locaiton):
#         pass
# supply_depot = BuildingUnit("서플라이디폿", 500, "7시") # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛 _스타크래프트 설명
# # pass 예제2
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
# def game_over():
#     pass
# game_start()
# game_over()

# #**9-9 super
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, locaiton):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # 상속받는 클래스의 멤버변수 가져올 때(생성자 호출할 때), 이렇게 super로도 사용 가능 
#         self.location = location
# # 다중상속일 때 super의 문제점
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")
# class Flyable: 
#     def __init__(self):
#         print("Flyable 생성자")
# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         super().__init__() # 다중상속 받을 경우, super는 처음 오는 클래스인 'Flyable'클래스의 __init__함수가 호출됨
# dropship = FlyableUnit() # 'Flyable 생성자'만 출력됨 