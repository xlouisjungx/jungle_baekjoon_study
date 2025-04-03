# 탑다운 방식

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print(fib_memo(10))  # Output: 55

# ---------------------------------------------------------------

# 바텀업 방식

def fib_bottom_up(n):
    if n <= 2:
        return 1
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib_bottom_up(10))  # Output: 55