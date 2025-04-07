def LCS(X, Y):
    X, Y = " " + X, " " + Y
    for i in range(1, len(X) - 1):
        for j in range(1, len(Y) - 1):
            if X[i] == Y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                backTrack[i][j] = 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                backTrack[i][j] = 2 if dp[i - 1][j] > dp[i][j - 1]
else 3