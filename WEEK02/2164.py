# ----- 선언 부분 -----
from collections import deque

N = int(input())
queue = deque(i+1 for i in range(N))

# ----- 문제 해결 부분 -----

while len(queue) != 1:
    # 우선, 제일 위에 있는 카드를 바닥에 버린다. 
    queue.popleft()
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
    num = queue.popleft()
    queue.append(num)

print(*queue)

# 예를 들어 N=4인 경우를 생각해 보자. 

# 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 

# 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 

# 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 

# 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.