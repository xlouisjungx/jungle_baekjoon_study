# ----- 선언 부분 -----
from collections import deque

N = int(input())
queue = deque()
result = []

# ----- 문제 헤결 부분 -----
for i in range(N):
    M = list(map(str, input().split()))
    
    if "push" in M:
        queue.append(M[-1])

    if "pop" in M:
        if len(queue) == 0:
            result.append(-1)
        else:
            cnt = queue.popleft()
            result.append(cnt)

    if "size" in M:
        result.append(len(queue))
    
    if "empty" in M:
        if len(queue) == 0:
            result.append(1)
        else :
            result.append(0)

    if "front" in M:
        if len(queue) == 0:
            result.append(-1)
        else :
            result.append(queue[0])

    if "back" in M:
        if len(queue) == 0:
            result.append(-1)
        else :
            result.append(queue[-1])

for i in range(len(result)):
    print(result[i])