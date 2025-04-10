# 첫째 줄에 두 정수 N, M(0 ≤ M ≤ N-2)이 주어진다. M은 크기가 맞지 않는, 즉 크기가 작은 돌의 개수이다. 
# 다음 M개의 줄에는 크기가 작은 돌들의 번호가 주어진다. 
# 1번 돌과 N번 돌은 충분히 크기가 크다고 가정한다.

import sys

Mini_Stones = []
Jump = [0] * 3
cnt = 1

N, M = map(int, sys.stdin.readline().strip().split())
Stones = [i for i in range(1, N+1)]

for i in range(M):
    MS = int(input())
    Mini_Stones.append(MS)

k = 1
i = 2

for i in range(i, N+2):
    Jump[0] = k + 1
    Jump[1] = k
    Jump[2] = k -1
    for j in range(3):
        if i + Jump[j] not in Mini_Stones:
        
            cnt += 1
            
            k = Jump[j]
            i += Jump[j]
            print("k의 상태 : ", k)
            print("위치 : ", i)
            print("현재 점프 수 : ", cnt)
            print("현재 점프 리스트 : ", Jump)
            
        else:
            pass

print("현재 돌들의 길이 : ", Stones)
print("작아서 못 넘어가는 돌들 : ", Mini_Stones)
print("최소 점프 수 : ", cnt)