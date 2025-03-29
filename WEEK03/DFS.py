# 재귀

def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)  # 방문 처리
        print(node, end=" ")  # 방문한 노드 출력
        for neighbor in graph[node]:  # 인접 노드 방문
            dfs_recursive(graph, neighbor, visited)

# 예제 그래프 (인접 리스트)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1, 7],
    5: [2],
    6: [2],
    7: [4]
}

visited = set()
print("DFS (재귀):", end=" ")
dfs_recursive(graph, 0, visited)

# ----------------------------------------------------------------------------------------

# 스택, 반복문

def dfs_stack(graph, start):
    visited = set()
    stack = [start]  # 스택 초기화

    while stack:
        node = stack.pop()  # 스택에서 노드 꺼내기
        if node not in visited:
            visited.add(node)  # 방문 처리
            print(node, end=" ")  # 방문한 노드 출력
            stack.extend(reversed(graph[node]))  # 인접 노드 추가 (역순으로 넣어야 순서 유지)

# 예제 그래프
print("\nDFS (스택):", end=" ")
dfs_stack(graph, 0)
