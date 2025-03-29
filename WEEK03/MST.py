# 크루스칼 알고리즘 기본 코드

class DisjointSet:
    """ 유니온-파인드 (서로소 집합) 자료구조 """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_mst(n, edges):
    """ 크루스칼 알고리즘을 사용한 MST 계산 """
    edges.sort(key=lambda x: x[2])  # 간선을 가중치 기준으로 정렬
    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):  # 사이클 방지
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# -----------------------------------------------------

# 프림 알고리즘 기본 코드

import heapq

def prim_mst(n, graph):
    """ 프림 알고리즘을 사용한 MST 계산 """
    visited = [False] * n
    pq = [(0, 0)]  # (가중치, 시작 노드)
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

    return mst, total_cost
