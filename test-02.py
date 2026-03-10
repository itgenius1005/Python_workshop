money = True
if money:
    print("택시를 탄다.")
else:
    print("걸어간다.")

a, b = 1, 2
if a < b:
    print("2보다 작다.")

if money:
    print("택시를")
    print("타고")

# x > y, x == y, x != y, x >= y, x <= y

money = 1000
card = True
if money >= 2000 or card:
    print("택시타고 간다.")
else:
    print("걸어간다.")

data = [1, 2, 3, 4, 5]
if 6 in data:
    print("3이 있다.")

data2 = ["이순신", "김유신", "강감찬"]
if "김유신" not in data2:
    print("김유신이 없다.")

data3 = [1, 2, 3, 4, 5] # 리스트
data4 = (1, 2, 3, 4, 5) # 튜플
data5 = {1, 2, 3, 4, 5} # 집합
datq6 = {"a": 1, "b": 2, "c": 3} # 딕셔너리

pocket = ["paper", "cellphone", "money"]
cart = True
if 'money' in pocket:
    print("택시를 타고 간다.")
elif card:
    print("카드를 꺼내서 택시를 타고 간다.")    
else:
    print("걸어간다.")

import
from random import randint

