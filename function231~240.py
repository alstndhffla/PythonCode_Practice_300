# 231
"""
문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의
make_url("naver")
www.naver.com
"""


def make_url(a):
    # url = "www." + a + ".com"
    # return url
    return print("www."+a+".com")


make_url("naver")


print("---------------")
# 233
"""
문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수
make_list("abcd")
['a', 'b', 'c', 'd']
"""


def make_list(a):
    list = []

    for i in range(len(a)):
        list.append(a[i])

    return list

    # or 바로 이렇게 사용도 가능.
    # return list(a)


print(make_list("money"))


print("------------")
# 234
"""
숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현
pickup_even([3, 4, 5, 6, 7, 8])
[4, 6, 8]
"""


def pickup_even(a):
    list1 = []
    for i in range(len(a)):
        if int(a[i]) % 2 == 0:
            list1.append(a[i])

    return list1


print(pickup_even([3, 4, 5, 6, 7, 8]))


# 235
print("-------------")
"""
콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
convert_int("1,234,567")
1234567
"""


def convert_int(a):
    return int(a.replace(',', ''))


print(convert_int("1,234,567"))
print(type(convert_int("1,234,567")))


# 237
print("-------------")
"""
결과값을 비교해라
"""


def 함수(num):
    return num + 4


a = 함수(10)
b = 함수(a)
c = 함수(b)
d = 함수(함수(함수(10)))

print(c)
print(d)


# 238
print("-------------")
"""
실행결과를 예측하라
"""


def 함수1(num):
    return num + 4


def 함수2(num):
    num = num + 2
    return 함수1(num)


c = 함수2(10)
print(c)


# 239
print("-------------")
"""
실행결과를 예측하라
"""


def 함수0(num):
    return num * 2


def 함수1(num):
    return 함수0(num + 2)


def 함수2(num):
    num = num + 10
    return 함수1(num)


c = 함수2(2)
print(c)
