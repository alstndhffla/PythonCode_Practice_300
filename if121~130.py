# 121
low = input("문자를 입력하세요:")
if low.islower():
    print(low.upper())
else:
    print(low)

# 122
score = input("점수를 입력하세요")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")

# 123
money = input("입력:")
change = money.split(" ")
exchange = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
if change[1] == "달러":
    print(int(change[0])*exchange.get("달러"), "원")
elif change[1] == "엔":
    print(int(change[0])*exchange.get("엔"), "원")
elif change[1] == "유로":
    print(int(change[0])*exchange.get("유로"), "원")
elif change[1] == "위안":
    print(int(change[0])*exchange.get("위안"), "원")

# 123 - 1
환율 = {"달러": 1167,
        "엔": 1.096,
        "유로": 1268,
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

# 124
num1 = input("number1:")
num2 = input("number2:")
num3 = input("number3:")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num2 and num3 > num1:
    print(num3)

# 125
# 010-345-1922
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

# 126 슬라이싱은 인덱싱이 아니라 자릿수.
우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
