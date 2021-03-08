# 151
print("----------------")
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print(i)

# 152
print("----------------")
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 == 0:
        print(i)

# 152
print("----------------")
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i < 20 and i % 3 == 0:
        print(i)

# 153 3글자 이상
print("----------------")
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i) >= 3:
        print(i)

# 154
print("----------------")
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)

# 154
print("----------------")
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.islower():
        print(i)

# 155 이름의 첫글자를 대문자로.
print("----------------")
리스트 = ['dog', 'cat', 'parrot', 'Home']
for i in 리스트:
    # print(i[0].islower())
    if i[0].islower():
        i[0].upper()
        print(i[0].upper() + i[1:])
    else:
        print(i)

# 156
print("----------------")
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
    print(i.split(".")[0])
    # k = i.split(".")
    # print(k)

# 159
print("-----------------")
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i.split(".")[1] in ["h", "c"]:
        print(i)