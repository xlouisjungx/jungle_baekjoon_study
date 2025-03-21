# ----- 선언 부분 -----
N = int(input())
numL = list(map(int, input().split()))

M = int(input())
comN = list(map(int, input().split()))

cnt = 0
result = []

# ----- 문제 해결 부분 -----
for i in range(M):
    cnt = 0
    if comN[i] in numL:
        cnt = numL.count(comN[i])
        result.append(cnt)

    else:
         result.append(0)
    
print(*result)