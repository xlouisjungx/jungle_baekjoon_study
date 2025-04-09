import sys

First_str = []
Second_str = []

First_str = list(map(str, sys.stdin.readline().strip()))
Second_str = list(map(str, sys.stdin.readline().strip()))

m, n = len(First_str), len(Second_str)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if First_str[i-1] == Second_str[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m][n])