def Pibo(n):
    if n <= 2:
        return 1
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]

n = int(input())
print(Pibo(n))