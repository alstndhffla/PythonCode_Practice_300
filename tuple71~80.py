# 71 튜플()
my_variable = ()
print(type(my_variable))


# 72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 73
num = (1)
print(type(num))
print(num)

# 74
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(type(data))

# 75
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(type(data))

# 76
data = tuple(range(2, 100, 2))
print(data)
