# ----- 선언 구간 -----
num = int(input())
numL = []
cnt = 0

# ----- 문제 해결 구간 -----
numL = list(map(int, input().split()))
numF = int(input())

for i in range(num):
    if numL[i] == numF:
        cnt += 1

print(cnt)