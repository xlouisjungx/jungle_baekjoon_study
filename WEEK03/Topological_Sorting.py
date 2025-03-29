#  Kahn's Algorithm (BFS 기반)

from collections import deque

def topological_sort_kahn(graph, in_degree):
    queue = deque([node for node in graph if in_degree[node] == 0])  # 진입 차수 0인 노드들
    result = []  # 위상 정렬 결과

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1  # 간선 제거
            if in_degree[neighbor] == 0:
                queue.append(neighbor)  # 새로 진입 차수 0이 된 노드 추가

    return result if len(result) == len(graph) else []  # 사이클 존재하면 실패

# 예제 DAG 그래프 (인접 리스트 & 진입 차수)
graph = {
    0: [1, 2],
    1: [3],
    2: [3, 4],
    3: [5],
    4: [5],
    5: []
}
in_degree = {i: 0 for i in graph}
for nodes in graph.values():
    for node in nodes:
        in_degree[node] += 1

print("위상 정렬 (Kahn 알고리즘):", topological_sort_kahn(graph, in_degree))

# -----------------------------------------------------------------------------------------------

#  DFS 기반 위상 정렬

def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        stack.append(node)  # 방문 완료 후 스택에 추가

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # 스택 역순으로 반환

print("위상 정렬 (DFS 기반):", topological_sort_dfs(graph))