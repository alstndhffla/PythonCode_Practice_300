# 21 파이썬 문자열에서 한글자씩 가져오는 걸 인덱싱이라고 한다.
letter = 'python'
print(letter[0], letter[2])

# 22
license_plate = "24가 2210"
print(license_plate[:])
print(license_plate[4:])
a = license_plate[4:]
print(a)
print(license_plate[-4:])
b = license_plate[-4:]
print(b)
print(license_plate[:4])
c = license_plate[:4]
print(c)
print(license_plate[:-4])
d = license_plate[:-4]
print(d)

# 23 시작인덱스:끝인덱스:오프셋
string = "홀짝홀짝홀짝"
print(string[0]+string[2]+string[4])
print(string[::2])

# 24
string = "PYTHON"
print(string[::-1])

# 25
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 26
phone_number2 = phone_number1.replace(" ", "")
print(phone_number2)

# 27
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split)
print(url_split[-1])
print(url_split[1])

# 28
string = 'abcdfe2a354a32a'
string1 = string.replace("a", "A")
print(string1)

# 34
t1 = 'python'
t2 = 'java'
print((t1 + t2)*4)
t3 = t1+' '+t2+' '
print(t3*4)

# 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s   나이: %d" % (name1, age1))
print("이름: %s   나이: %d" % (name2, age2))

print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

# 3.6 부터 지원하는 f-string
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 38
상장주식수 = "5,969,782,550"
int_상장주식수 = int(상장주식수.replace(",", ""))
print(int_상장주식수, type(int_상장주식수))


# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])
print(분기[:7])

# 40
data = "   삼성전자    "
data1 = data.strip()
print(data)
print(data1)

# 41
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
ticker2 = ticker.lower()
print(ticker2)

# 42
a = "Hello"
a = a.capitalize()
print(a)

# 43 True or False
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 44
file_name1 = "2020_보고서.xlsx"
print(file_name1.startswith("2020_-"))

# 45
a = "hello world"
b = a.split()
c = a.split(" ")
print(b)
print(c)

# 50
data = "039490     "
data1 = data.rstrip()
print(data)
print(data1)
