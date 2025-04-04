import sys

def Min_Coins(N, K, coins):
    
    cnt = 0

    for i in range(N):
        while K - coins[i] >= 0:
            K -= coins[i]
            cnt += 1
    
    return cnt

N, K = map(int, sys.stdin.readline().strip().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]

coins.sort(reverse=True)

print(Min_Coins(N, K, coins))