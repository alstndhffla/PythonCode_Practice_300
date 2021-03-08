# 181
"""
101호	102호
201호	202호
301호	302호
"""
apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]

# 182
"""
100	80
200	210
300	330
"""
stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

# 183
"""
100	80
200	210
300	330
"""
value = {"시가": [100, 200, 300], "종가": [80, 210, 330]}

# 184
stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}

# 185
apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
for i in range(len(apart)):
    print(apart[i][0])
    print(apart[i][1])

for row in apart:
    # row = ['101호', '102호']
    for col in row:
        # col = ['101호']
        print(col, "호")

# 186
"""
301 호
302 호
201 호
202 호
101 호
102 호
"""
apart = [[101, 102], [201, 202], [301, 302]]
print(len(apart))
for i in range(len(apart), 0, -1):
    print(apart[i-1][0])
    print(apart[i-1][1])


for row in apart[::-1]:
    for col in row:
        print(col, "호")

# 187
"""
101 호
-----
102 호
-----
201 호
-----
202 호
-----
301 호
-----
302 호
-----
"""
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    for k in i:
        print(k, "호")
        print("------")


# 189
"""
101 호
102 호
-----
201 호
202 호
-----
301 호
302 호
-----
"""
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    print(i[0])
    print(i[1])
    print("---------")

for row in apart:
    for col in row:
        print(col, "호")
    print("-----")

# 190
"""
101 호
102 호
201 호
202 호
301 호
302 호
-----
"""
apart = [[101, 102], [201, 202], [301, 302]]
for i in apart:
    print(i[0])
    print(i[1])
print("--------")

for row in apart:
    for col in row:
        print(col, "호")
print("-" * 5)


