# 221
"""
입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의
"""


def print_reverse(string):
    print(string[::-1])


print_reverse("python")


# 222
"""
성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의
"""
print("-----------------")

"""
def print_score(score_list):
    print(sum(score_list)/len(score_list))
"""


def print_score(a):
    sum1 = 0
    for i in a:
        sum1 = i + sum1

    print(sum1/len(a))


print_score([1, 2, 3])

# 223
"""
하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의
"""
print("-----------------")


def print_even(b):
    for i in b:
        if i % 2 == 0:
            print(i)


print_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 224
"""
하나의 딕셔너리를 입력받아 딕셔너리의 key 값만 화면에 출력하는 print_keys 함수를 정의하라.
"""
print("-----------------")


def print_keys(a):
    for keys in a.keys():
        print(keys)


print_keys({'이름': '김민수', "나이": 30, "성별": 0})


# 225
"""
my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

ex) [100, 130, 100, 100]
"""
print("-----------------")

my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]
           }


def print_value_by_key(my_dict, key):
    print(my_dict[key])


print_value_by_key(my_dict, "10/26")


# 225 -1
print("-----------------")


def vartest(a):
    a = a + 1


vartest(3)
# 아무것도 출력되지 않는다.


# 226






















