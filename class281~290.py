# 281
class car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


car1 = car(2, 1000)
print(car1.wheel)
print(car1.price)


print("-------------------")
# 282
"""
차 클래스를 상속받은 자전차 클래스를 정의
코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속
"""


class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


bicycle = 자전차(2, 100)
print(bicycle.가격)
