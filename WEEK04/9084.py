import sys

T = int(sys.stdin.readline()) # 테스트 케이스 수

Coin_List = [] # 동전 리스트
How_many = [] # 경우의 수 리스트

for i in range(T):
    
    N = int(sys.stdin.readline()) # 동전 종류 개수
    Coin_List = list(map(int, sys.stdin.readline().split())) # 동전 종류 개수 입력
    coin = int(sys.stdin.readline()) # 계산할 동전 입력

    dp = [0] * (coin+1) # 경우의 수 공간 생성
    dp[0] = 1 # 아무 동전도 사용하지 않을 때의 경우
    
    for coin_type in Coin_List: # for문이 하나씩 추가될떄마다, 새로운 조합을 추가 / 2원을 사용하는 경우, 기존에 dp[i-2]원이 거기에 있다면, 거기에 2월을 더해서 만들 수 있다.
        for j in range(coin_type, coin+1):
            
            # dp[j - coin_type] = 현재 동전을 사용하기 전, coin_type원을 제외한 금액을 만드는 방법의 수
            dp[j] += dp[j - coin_type] # coin_type원을 추가로 사용해서 j원을 만드는 경우를 누적. 

    How_many.append(dp[coin])

# 출력
for i in range(len(How_many)):
    print(How_many[i])