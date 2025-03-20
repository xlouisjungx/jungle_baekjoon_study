# ----- 선언 부분 -----
N = int(input())
numL = []
total = 0

# ----- 문제 해결 부분 -----
numL = list(map(int, input()))
for i in range(N):
    total += numL[i]

print(total)