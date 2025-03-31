# ----- 선언 부분 -----
import sys

def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for i in graph[node]:
            dfs(graph, i, visited)

K = int(input())

# ----- 해결 부분 -----
graph = [[] for _ in range(K+1)]
visited = [0 for _ in range(K+1)]

for i in range((K-1)):
    V, E = map(int, sys.stdin.readline().split())
    graph[V].append(E)
    graph[E].append(V)

dfs(graph, 0, visited)