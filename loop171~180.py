# 171
print('---------------')
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

# 172
print('---------------')
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])

for i, data in enumerate(price_list):
    print(i, data)

# 173
print('---------------')
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

# 174
print('---------------')
num = 90
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    num = num + 10
    print(num, price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

# 175
print('---------------')
my_list = ["가", "나", "다", "라"]
for i in range(0, 3):
    print(my_list[i], my_list[i+1])

for i in range(1, len(my_list)):
    print(my_list[i-1], my_list[i])

# 176
print('---------------')
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list) - 2):
    print(my_list[i], my_list[i+1], my_list[i+2])

for i in range(1, len(my_list) - 1):
    print(my_list[i-1], my_list[i], my_list[i+1])

for i in range(2, len(my_list)):
    print(my_list[i - 2], my_list[i - 1], my_list[i])

# 177
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])

for i in range(len(my_list) - 1):
    print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

# 178
my_list = [100, 200, 400, 800]
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

# 180
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for i in range(0, len(low_prices)):
    vol = high_prices[i] - low_prices[i]
    volatility.append(vol)

print(volatility)

volatility1 = []
for i in range(len(low_prices)):
    volatility1.append(high_prices[i] - low_prices[i])

print(volatility1)


