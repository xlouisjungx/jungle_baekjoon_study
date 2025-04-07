def LCS(X, Y): # 수열 X와 Y의 최장 공통 부분 수열(LCS)의 길이
    m, n = len(X), len(Y)
    if m == 0 or n == 0:
        return 0
    else:
        if X[-1] == Y[-1]:
            return LCS(X[:m-1], Y[:n-1]) + 1
        else:
            return max(LCS(X,Y[:n-1]), LCS(X[:m-1], Y))