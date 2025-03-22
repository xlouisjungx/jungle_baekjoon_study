# ----- 선언 부분 -----
import sys
input = sys.stdin.readline

N = int(input())
numL = [int(input()) for _ in range(N)]

maxN = 0
cnt = 0

# ----- 문제 해결 부분 -----
    
for i in range(N-1, -1, -1):
    if maxN < numL[i]:
        maxN = numL[i]
        cnt += 1

print(cnt)