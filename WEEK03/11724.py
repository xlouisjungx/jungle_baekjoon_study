# ----- 선언 부분 -----
import sys

sys.setrecursionlimit(10000) 

def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def connected_components(graph, N):
    visited = [False] * (N + 1)
    components = []
    
    for node in range(1, N + 1):
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    
    return components

# ----- 문제 해결 부분 -----
N, M = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}

visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

print(len(connected_components(graph, N)))

# 런타임 오류는 connected_components 함수에서 연결 요소를 구하는 과정에서, 
# component 리스트가 사실상 사용되지 않고 빈 리스트로만 추가되고 있다는 점입니다. 
# 그리고 dfs 함수 내에서 방문한 노드만 추적하며 연결된 노드를 탐색하지만, component 리스트는 채워지지 않습니다.

# dfs 함수에서 각 노드를 component에 추가: 현재 dfs 함수에서는 방문만 추적하고 있지만, 
# 연결된 노드를 component에 추가하여 연결 요소를 구할 수 있도록 해야 합니다.
# component 리스트를 올바르게 채우기: 각 DFS 호출 시 방문한 노드를 component에 추가하여 연결 요소에 포함된 노드를 추적해야 합니다.

# 그래프의 크기가 크고, 연결 요소가 깊게 재귀를 타게 되면 RecursionError가 발생할 수 있습니다.
# 파이썬의 기본 재귀 제한은 1000번인데, 이 값 이상으로 깊은 재귀를 사용하면 오류가 발생합니다.