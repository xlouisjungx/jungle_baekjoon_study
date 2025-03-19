# ----- 선언 부분 -----
N, X = map(int, input().split())
numL = 0
result = []

# ----- 문제 해결 부분 -----
numL = list(map(int, input().split()))

for i in range(N):
    if numL[i] < X:
        result.append(numL[i])

for i in range(len(result)):
    if i < len(result)-1: 
        print(result[i], end=' ')
    else:
        print(result[i])
        break