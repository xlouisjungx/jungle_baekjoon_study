from collections import deque

def bfs(graph, start):
    visited = set()  # 방문한 노드를 저장
    queue = deque([start])  # BFS에 사용할 큐 (FIFO)

    while queue:
        node = queue.popleft()  # 큐에서 노드 꺼내기
        if node not in visited:
            visited.add(node)  # 방문 처리
            print(node, end=" ")  # 방문한 노드 출력
            queue.extend(graph[node])  # 인접 노드 큐에 추가

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

print("BFS 탐색 순서:", end=" ")
bfs(graph, 0)