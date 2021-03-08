# 161
for i in range(100):
    print(i)

# 162
for i in range(2002, 2051, 4):
    print(i)

# 163
print('---------------')
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

# 163 -1
for num in range(3, 31, 3):
    print(num)


# 164
print('---------------')
for i in range(100):
    print(99-i)

# 165
print('---------------')
for i in range(10) :
    print(i / 10)

# 166
print('---------------')
for i in range(1, 10):
    print("3 *", i, "=", 3*i)

#
for i in range(1, 10):
    print(3, "x", i, " = ", 3 * i)

# 167
print('---------------')
for i in range(1, 10, 2):
    print("3 *", i, "=", 3 * i)

for i in range(1, 10) :
    if i % 2 == 1 :
        print(3, "x", i, " = ", 3 * i)

# 168 숫자를 모두 더한 값.
print('---------------')
sum = 0
for i in range(1, 11):
    sum = i + sum
print(sum)

# 숫자를 모두 곱한 값
result = 1
for i in range(1, 11):
    result *= i     # result = result * i
print(result)