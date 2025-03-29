# ----- 선언 부분 -----
from collections import deque
import sys

# DFS (재귀 ver)
def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)  # 방문 처리
        print(node, end=" ")  # 방문한 노드 출력
        for neighbor in sorted(graph[node]):  # 인접 노드 방문
            dfs_recursive(graph, neighbor, visited)


# BFS
def bfs(graph, start):
    visited = set()  # 방문한 노드를 저장
    queue = deque([start])  # BFS에 사용할 큐 (FIFO)

    while queue:
        node = queue.popleft()  # 큐에서 노드 꺼내기
        if node not in visited:
            visited.add(node)  # 방문 처리
            print(node, end=" ")  # 방문한 노드 출력
            for i in sorted(graph[node]):
                queue.append(i)  # 인접 노드 큐에 추가

# ----- 문제 해결 부분 -----

N, M, V = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    num1, num2 = map(int, sys.stdin.readline().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

visited = set()

dfs_recursive(graph, V, visited)
print()
bfs(graph, V)
print()