# ----- 선언 부분 -----
N, M = list(map(int, input().split()))
numL = [0] * N

# ----- 문제 해결 부분 -----
for j in range(M):
    i, j, k = list(map(int, input().split()))
    for o in range(i-1, j):
        numL[o] = k

for i in range(N):
    if i < N-1:
        print(numL[i], end=" ")
    else:
        print(numL[i])