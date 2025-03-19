# ----- 선언 부분 -----
N, M = list(map(int, input().split()))

numL = []
chN = 0

# ----- 문제 해결 부분 -----
for i in range(N):
    numL.append(i+1)

for k in range(M):
    i, j = list(map(int, input().split()))
    chN = numL[i - 1]
    numL[i-1] = numL[j-1]
    numL[j-1] = chN

for i in range(N):
    if i < N - 1:
        print(numL[i], end=" ")
    else:
        print(numL[i])