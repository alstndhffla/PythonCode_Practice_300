# 211
print("-------------")


def function(f):
    print(f)


function("안녕")
function("Hi")


# 212
print("-------------")


def plus(a, b):
    print(a + b)


plus(3, 4)
plus(7, 8)


# 213
print("-------------")
"""
오류 난다. 함수 매개변수에 들어갈 값이 없기 때문 
"""
#
#
# def 함수(문자열):
#     print(문자열)
#
#
# 함수()

# 214
print("-------------")
"""
하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
"""


def print_with_smile(f):
    print(f + ":D")


print_with_smile("안녕")


# 215
print("-------------")
"""
현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의
"""


def print_upper_price(o):
    # print(o + o * 0.3)
    print(o * 1.3)


print_upper_price(100)

# 216
print("-----------")
"""
두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의
"""


def print_sum(c, d):
    print(c+d)


print_sum(5, 5)

# 217
print("-----------")
"""
두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성
"""


def print_arithmetic_operation(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)


print_arithmetic_operation(10, 10)

# 217
print("-----------")
"""
세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
"""


def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > c and b > a:
        print(b)
    elif c > a and c > b:
        print(c)
    """
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)
    """


print_max(10, 100, 1000)
