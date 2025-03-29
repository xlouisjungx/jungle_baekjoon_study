# ----- 선언 부분 -----
import heapq
import sys

def prim_mst(n, graph):
    """ 프림 알고리즘을 사용한 MST 계산 """
    visited = [False] * (n+1)
    pq = [(0, 1)]  # (가중치, 시작 노드)
    mst = []
    total_cost = 0

    while pq:
        weight, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight

        for v, w in graph[u]:  # 인접 노드 탐색
            if not visited[v]:
                heapq.heappush(pq, (w, v))
                mst.append((u, v, w))

    return total_cost

# ----- 문제 해결 부분 -----
V, E = map(int, input().split())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 무방향 그래프

print(prim_mst(V, graph))