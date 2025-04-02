# 블로그 참고하여 품. 추후 복습 및 닷 풀기 계획

# ----- 선언 부분 -----
import sys
from collections import deque

def odd(N):
    return 1 if N % 2 == 0 else -1

def bfs(current):
    queue = deque()
    level = 0
    queue.append((current, level+1))
    vst[current] = odd(level)

    while queue:
        now = queue.popleft()
        c_node, level = now
        
        for i in adj_list[c_node]:
            if not vst[i]:
                queue.append((i, level+1))
                vst[i] = odd(level)

            elif vst[i] == odd(level):
                continue

            elif vst[i] != odd(level):
                return False
            
    return True

# ----- 해결 부분 -----
k = int(input())
result = []
for _ in range(k):
    vertex, edge = map(int, input().split())
    adj_list = [[] for _ in range(vertex+1)]
    for _ in range(edge):
        u, v = map(int, sys.stdin.readline().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    vst = [0]*(vertex+1)

    graph_list = []
    for i in range(1, vertex+1):
        if not vst[i]:
            graph_list.append(bfs(i))

    if all(graph_list):
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)