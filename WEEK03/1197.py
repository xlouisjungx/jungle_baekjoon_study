import heapq

def prim(n, edges):
    # 그래프를 인접 리스트로 변환
    graph = {i: [] for i in range(n)}  # n은 정점의 수
    for u, v, weight in edges:
        graph[u].append((v, weight))  # u -> v
        graph[v].append((u, weight))  # v -> u (무방향 그래프)

    # MST에 포함된 간선과 가중치
    mst = []
    mst_weight = 0

    # 방문한 정점들
    visited = [False] * n

    # 우선순위 큐 (가중치, 정점)
    min_heap = [(0, 0)]  # (가중치, 시작 정점 0)

    while min_heap:
        weight, u = heapq.heappop(min_heap)  # 가중치가 가장 작은 간선 선택
        
        if visited[u]:  # 이미 방문한 정점이면 무시
            continue
        
        visited[u] = True  # 정점 u를 MST에 포함시킴
        mst.append((u, weight))  # (정점, 가중치)
        mst_weight += weight  # MST의 가중치 합 업데이트

        # u와 연결된 간선들을 큐에 추가
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))  # 연결된 간선들을 큐에 추가

    return mst, mst_weight

# 예시
V, C = map(int, input().split())

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]  # 간선 (u, v, 가중치)

mst, mst_weight = prim(n, edges)
print("최소 스패닝 트리:", mst)
print("MST의 총 가중치:", mst_weight)