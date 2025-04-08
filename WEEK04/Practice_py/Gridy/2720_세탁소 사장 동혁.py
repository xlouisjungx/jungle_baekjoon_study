# 브론즈 3 문제

# 거스름돈의 액수가 주어지면 리암이 줘야할 
# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수

import sys

# / (나누기, 실수 나눗셈) --> 결과가 소수점까지 나오는 실수
# // (몫 나누기, 정수 나눗셈) --> 결과가 소수점 이하를 버린 정수 --> 몫만 구한다!

def Change_Money(money):
    Quarter = money // 25
    money = money % 25
   
    Dime = money // 10
    money %= 10
   
    Nickel = money // 5
    money %= 5
   
    Penny = money // 1
    money %= 1
    
    changed_money.append((Quarter, Dime, Nickel, Penny))

changed_money = []

T = int(sys.stdin.readline())
for i in range(T):
    money = int(sys.stdin.readline())
    Change_Money(money)

for i in range(len(changed_money)):
    print(*changed_money[i])