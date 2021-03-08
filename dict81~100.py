# 81 별 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

# 82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)

# 83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, c = scores
print(valid_score)

# 84
temp = {}
print(type(temp))

# 85
temp = {"메로니": 1000, "폴라포": 1200, "빵빠레": 1800}
print(temp)

# 86
temp["죠스바"] = 1200
temp["월드콘"] = 1500
print(temp)

# 87
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print("메로나 가격: ", ice["메로나"])

# 88
ice["메로나"] = 1300
print(ice)

# 89
del ice["메로나"]
print(ice)

# 91
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

# 92
print(inventory["메로나"][0], "원")

# 93
print(inventory["메로나"][1], "개")

# 94

inventory["월드콘"] = [500, 7]
print(inventory)

# 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
print(ice)

# 96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(ice)

# 97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.values())
print(sum(ice))

# 98 dict 은 update, list는 append 로 추가한다.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream.update(new_product))     # 바로 출력은 안됨.
print(icecream)

# 99 zip과 dict 두개의 튜플을 하나의 딕셔너리로.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)

