# 251
"""
클래스는 설계도면
객체는 클래스로 만든 제품(객체마다 고유한 특성을 가질 수 있다.)

객체와 인스턴스의 차이
클래스로 만든 객체를 인스턴스라고도 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까?
이렇게 생각해 보자. a = Cookie() 이렇게 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다.
즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
"a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 "a는 Cookie의 객체"보다는
"a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울린다.

"""

# 252
"""
비어있는 사람 (Human) 클래스를 "정의" 
사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가
"""


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("응애응애")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # Human 클래스를 인스턴스화 할시 해당 코드 자동 실행됨(생성자)
    def __del__(self):
        print("나의 죽음을 알리지마라")


# 253
"""
사람 클래스의 인스턴스를 "생성"하고 이를 areum 변수로 바인딩
"""
# 1
areum = Human("조아름", 25, "여자")
print(areum.name)
areum.who()
# del areum     # 따로 입력할 필요 x?! __del__ 생성자 뭐임.

# 2 위에서 areum 이란 객체를 삭제했기 때문에 해당 객체를 재사용하려면 다시 Human 클래스의 인스턴스 'areum'로 만들어줘야한다.
areum = Human("조아름", 25, "여자")
areum.setInfo("아름", 25, "여자")
areum.who()









# 254
"""
사칙연산 계산기
"""


class FourCal:
    # pass  # pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용한다.
    # 클래스 안 함수 -> "메서드" 라 부른다.
    """
    메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다.
    예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다.
    메서드 이름으로 __init__ 사용하면 됨. -> 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되게 하는 메서드
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return print(result)

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return print(result)


a = FourCal(4, 2)
a.add()
print(a.first)
print(a.second)
a.div()


# 260
class OMG:
    def print(self):
        print("Oh my god")


# 1
mystock = OMG()
mystock.print()

# 2
OMG.print(mystock)