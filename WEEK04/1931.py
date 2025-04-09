# 골드 V 문제

import sys

Room = []
cnt = 1

N = int(sys.stdin.readline())

for i in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    Room.append((start, end))
    
Room.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간이 같을 경우에도 시작 시간이 빠른 회의를 먼저 넣어야, 더 많은 회의를 넣을 수 있다.
                                      # --> 튜플 정렬
# 먼저 두번째값을 먼저 정렬하고, 정렬하다가 같은 두번째이 발견되면, 거기서는 첫번째 값으로 오름차순 정렬을 한다.

start_time = 0
end_time = Room[0][1]

for i in range(1, N):
    start_time = Room[i][0]
    if end_time <= start_time: # 끝나는 시간 / 새롭게 시작하는 시간
        end_time = Room[i][1]
        cnt += 1
        
print(cnt)