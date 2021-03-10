import csv

# 291
"""
바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 쓰기
"""
f = open("C:/Users/alstn/Desktop/매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()


print("--------------")
# 292
f = open("C:/Users/alstn/Desktop/매수종목2.txt", mode="wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER\n")
f.close()


print("--------------")
# 293
f = open("C:/Users/alstn/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
writer = csv.writer(f)
writer.writerow(["종목명", "종목코드", "PER"])
writer.writerow(["삼성전자", "005930", 15.59])
writer.writerow(["NAVER", "035420", 55.82])
f.close()


print("--------------")
# 294
"""
바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장
005930
005380
035420
"""
f = open("C:/Users/alstn/Desktop/매수종목1.txt", encoding="utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()  # '\n'
    codes.append(code)

print(codes)
f.close()


print("--------------")
# 295
"""
바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장. 
종목명을 key 로 종목명을 value 로 저장
005930 삼성전자
005380 현대차
035420 NAVER
"""
f = open("C:/Users/alstn/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()     # '\n' 제거
    k, v = line.split()
    # print(k, v)
    data[k] = v

print(data)
f.close()


print("--------------")
# 296
"""
문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생. 
예외처리를 통해 에러가 발생하는 PER은 0으로 출력
"""
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)


print("--------------")
# 297
"""
문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장
"""
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)

print(new_per)


print("--------------")
# 298
"""
어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생. 
try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리
"""

try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안됨")


print("--------------")
# 299
"""
리스트의 인덱싱에 대해 에러를 출력
"""
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)


# 300
"""
-----------------------------------------
try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드
-----------------------------------------
    
per = ["10.31", "", "8.00"]

for i in per:
    print(float(per))
    
    
"""
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")

