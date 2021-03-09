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
"""
입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수
print_5xn("아이엠어보이유알어걸")
아이엠어보
이유알어걸
"""


def print_5xn(line):
    # 1
    print(line[:5])
    print(line[5:])
    # 2
    chunk_num = int(len(line) / 5)
    print("chunk_num: ", chunk_num)
    for x in range(chunk_num + 1):
        print("x:", x)
        print(line[x * 5: x * 5 + 5])


print_5xn("아이엠어보이유알어걸히이즈어몬스터")

# 227
"""
문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성
print("아이엠어보이유알어걸", 3)
"""


def print_mxn(line, b):
    c = int(len(line)/b)
    for i in range(c+1):
        print(line[i*b:i*b+b])


print_mxn("아이엠어보이유알어걸", 3)

# 228
"""
연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 
회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림
calc_monthly_salary(12000000)
1000000
"""
print("------------")


def calc_monthly_salary(a):
    # print(annual_salary/12)
    sal = int(a/12)
    return print(sal)


calc_monthly_salary(12000000)


# 229
print("------------")
"""
코드의 실행결과 예측하라.
"""


def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)


# 1
my_print(a=100, b=200)
# 2
my_print(100, 200)
# 3
my_print(b=100, a=200)













