# 141
num = [100, 200, 300]
for i in num:
    print(i+10)

# 142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:", i)

# 143 문자열의 길이 출력.
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

# 144 동물이름과 글자수 출력
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

# 145 동물이름의 첫글자
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[:1])

리스트 = ['dog', 'cat', 'parrot']
for 이름 in 리스트:
    print(이름)
    print(이름[0])
    print(이름[1])
    print(type(이름[0]))
    print("----------------")

# 146
print("----------------")
리스트 = [1, 2, 3]
for i in 리스트:
    print("3 *", i)


# 147
print("----------------")
리스트 = [1, 2, 3]
for i in 리스트:
    print("3 *", i, "=", 3*int(i))

# 148
print("----------------")
리스트 = ["가", "나", "다", "라"]
슬라이싱 = 리스트[1:]
for i in 슬라이싱:
    print(i)

# 149
print("----------------")
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::2]:
  print(i)

# 150
print("----------------")
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
    print(i)

