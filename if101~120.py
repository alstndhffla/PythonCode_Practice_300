# 111
user = input("입력: ")
print(user*2)

# 112
num = input("숫자를 입력하세요: ")
print(int(num)+10)

# 113
nums = input("숫자입력: ")
if int(nums) % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 114
plus = input("입력값: ")
pp = int(plus)+20
if pp > 255:
    print(255)
else:
    print(pp)

# 115
v = input("입력값:")
m = int(v)-20
if m > 255:
    print(255)
elif m < 0:
    print(0)
else:
    print(m)

# 116
time = input("현재 시간 입력: ex.09:00")
# print(time[3:])
if time[3:] == 00:
    print("정각입니다.")
else:
    print("정각이 아닙니다.")

# 117
fruit = ["사과", "포도", "홍시"]
fav = input("좋아하는 과일은?:")
if fav in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
warn = input("검사할 투자경고종목을 입력하세요:")
if warn in warn_investment_list:
    print("투자경고종목입니다.")
else:
    print("투자경고종목이 아닙니다.")

# 119 키값
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
chk = input("당신이 좋아하는 계절을 입력흐세요:")
if chk in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

# 120 딕셔너리값
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")





