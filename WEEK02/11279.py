# ----- 선언 부분 -----
from collections import deque

N = int(input())
queue = deque()
result = []

# ----- 문제 해결 부분 -----
for i in range(N):
    num = int(input())

    if num > 0:
        queue.append(num)

    if len(queue) == 0 and num == 0:
        queue.append(0)

    if len(queue) != 0 and num == 0:

        queue = deque(sorted(queue, reverse=True))
        numX = queue.popleft()
        result.append(numX)

for i in range(len(result)):
    print(result[i])