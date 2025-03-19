# ----- 선언 부분 -----
N = 10
numL = []
cnt = 1

# ----- 문제 해결 부분 -----
for i in range(N):
    num = int(input())
    num = num % 42
    numL.append(num)

numL.sort()

for i in range(N-1):
    if numL[i] != numL[i+1]:
        cnt += 1

print(cnt)