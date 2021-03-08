# 191
"""
수수료 0.014% (*0.00014)
한라인에 하나씩 가격을 출력.

"""
data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
# print(data[0][0])
for i in range(len(data)):
    # print(len(data)+1)
    for k in range(len(data)+1):
        # print(data[i][k])
        # print(data[i][k]*0.014)
        print(data[i][k] + data[i][k]*0.00014)
        print("------------")


for line in data:
    for column in line:
        print(column * 1.00014)

# 192
"""
2000.28
3050.427
2050.2870000000003
1980.2772
----
7501.05
2050.2870000000003
2050.2870000000003
1980.2772
----
15452.163
15052.107
15552.177
14902.086000000001
----
"""
for i in range(len(data)):
    # print(len(data)+1)
    for k in range(len(data)+1):
        # print(data[i][k])
        # print(data[i][k]*0.014)
        print(data[i][k] + data[i][k]*0.00014)
    print("------------")

# 193
"""
print(result)
[2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, ...]
"""
result = []
data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in range(len(data)):
    # print(len(data)+1)
    for k in range(len(data)+1):
        # print(data[i][k])
        # print(data[i][k]*0.014)
        result.append(data[i][k] + data[i][k]*0.00014)
    print("------------")
print(result)

# 194
"""
>> print(result)
[
 [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
 [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
 [15452.163, 15052.107, 15552.177, 14902.086000000001]
]
"""
result = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)

# 195
"""
100
190
310
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    print(row[3])

# 196
"""
종가가 150원보다 큰 경우만 출력
"""
print("-------------")
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] > 150:
        print(i[3])

for row in ohlc[1:]:
    if row[3] > 150:
        print(row[3])

# 197
"""
종가가 시가보다 크거나 같은 경우에만 출력.
"""
print("-------------")
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    if i[3] >= i[0]:
        print(i[3])

for row in ohlc[1:]:
    if row[3] > row[0]:
        print(row[3])

# 198
print("-------------")
"""
고가와 저가의 차이를 변동폭으로 정의해 volatility 이름의 리스트에 저장하라.
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for i in ohlc[1:]:
    volatility.append(int(i[1])-int(i[2]))
print(volatility)

# 199
print("-------------")
"""
리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# print(int(i[3]))
# print(type(int(i[3])))
print(type(ohlc[0][0]))
for i in ohlc[1:]:
    print(type(i[3]))
    # if int(i[3]) - int(i[0]) > 0:     # 이것도 가능.
    if i[3] - i[0] > 0:
        print(i[1]-i[2])

# 200
print("-------------")
"""
리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 3일동안 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
"""
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

sum = 0
for i in ohlc[1:]:
    sum = i[3]-i[0] +sum

print(sum)

profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)
