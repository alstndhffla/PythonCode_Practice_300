# 201
def print_coin():
    print("비트코인")


# 202
print_coin()

# 203
"""
100번 호출
"""
print("-----------")
for i in range(1, 101):
    print_coin()


# 204
print("-----------")


def print_coins():
    # for i in range(1, 101):   # 이것도 사용가능
    for i in range(100):
        print_coin()


print_coins()

# 209
print("-----------")
"""
결과 예측해보셈
"""


def message1():
    print("A")


def message2():
    print("B")
    message1()


message2()
