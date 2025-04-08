# 골드 V 문제

import sys

Room = []
cnt = 0

N = int(sys.stdin.readline())

for i in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    Room.append((start, end))

Start_time = 0
End_Time = 0

for i in range(N):
    
    
print(cnt)