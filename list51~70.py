# 51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 52
movie_rank.append("배트맨")

# 53
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
movie_rank.insert(0, "조커")
print(movie_rank)

# 54
movie_rank.remove("럭키")
print(movie_rank)

# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 57
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print(min(nums))

# 58
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 60
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63
print(nums[1::2])

# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
inter = " ".join(interest)
print(type(inter))
# 공백을 사이사이에 넣어서 출력함.
print(" ".join(interest))

# 67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 68
print("\n".join(interest))

# 69
string = "삼성전자/LG전자/Naver"
a = string.split("/")
print(a)

# 70
data = [2, 4, 3, 1, 5, 10, 9]
# 오름차순
data.sort()
data1 = data.sort()
# 처리한 후 넣어야 한다.
print(data)
print(data1)
print(data.sort())

data2 = [2, 4, 3, 1, 5, 10, 9]
data3 = sorted(data)
print(data3)



