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

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        super().정보()
        print("구동계 ", self.구동계)


class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수:", self.바퀴)
        print("가격:", self.가격)

"""
bicycle = 자전차(2, 100)
print(bicycle.가격)
"""

print("-------------------")
car = 자동차(4, 1000)
car.정보()


# 286
print("-------------------")
"""
다음 코드가 동작하도록 자전차 클래스를 수정
>> bicycle = 자전차(2, 100, "시마노")
>> bicycle.정보()
바퀴수 2
가격 100
"""
bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 288
print("-------------------")


class 부모:
    def 호출(self):
        print("부모호출")


class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출()


# 289
print("-------------------")


class 부모:
    def __init__(self):
        print("부모생성")


class 자식(부모):
    def __init__(self):
        print("자식생성")


나 = 자식()


# 289
print("-------------------")


class 부모:
    def __init__(self):
        print("부모생성")


class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()


나 = 자식()