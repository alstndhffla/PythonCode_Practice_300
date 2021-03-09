# 261
"""
주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의
Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의
객체에 종목명을 입력할 수 있는 set_name 메서드를 추가
객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가
종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력
생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입
PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가
"""


class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend    # 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


# 1
# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)

# 2
# print("----------------")
# a = Stock(None, None)
# a.set_name("삼성전자")
# print(a.name)
#
# # 3
# print("----------------")
# b = Stock(None, None)
# b.set_code("005930")
# print(b.code)
#
# # 4
# print("----------------")
# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)
# print(삼성.get_name)  # 객체가 저장된 주소값
# print(삼성.get_code)  # 객체가 저장된 주소값
# print(삼성.get_name())
# print(삼성.get_code())

# 5
print("----------------")
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.dividend)

# 6
print("----------------")
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)   # 이미 있는 객체에 값을 바꿔서 출력.
print(삼성.per)

# 7
print("----------------")
"""
종목명	종목코드	PER	PBR	배당수익률
삼성전자	005930	15.79	1.33	2.83
현대차	005380	8.70	0.35	4.27
LG전자	066570	317.34	0.69	1.37
아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장 
파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력
"""
삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목 = [삼성전자, 현대차, LG전자]
"""
or 위 코드 대신에 이렇게 해도 됨.
종목.append(삼성전자)
종목.append(현대차)
종목.append(LG전자)
"""

for i in range(len(종목)):
    print("종목명:", 종목[i].name, 종목[i].code, 종목[i].per)
# 위아래 둘 다 같은 거.
for i in 종목:    # 리스트 안 종목별로 반복.
    print(i.code, i.per)
