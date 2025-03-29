# 인접 리스트(Adjacency List) 구현

class Graph:
    def __init__(self):
        self.graph = {}  # 인접 리스트로 그래프 저장

    def add_edge(self, u, v, directed=False):
        """ 간선 추가 (directed=True면 방향 그래프) """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []  # 무방향 그래프라면 필요

        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)  # 무방향 그래프라면 반대 방향도 추가

    def print_graph(self):
        """ 그래프 출력 """
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# 예제 그래프 생성
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print("인접 리스트 방식 그래프:")
g.print_graph()

# --------------------------------------------------------------------------

# 인접 행렬(Adjacency Matrix) 구현

class GraphMatrix:
    def __init__(self, size):
        self.size = size
        self.graph = [[0] * size for _ in range(size)]  # 2D 행렬 초기화

    def add_edge(self, u, v, directed=False):
        """ 간선 추가 (directed=True면 방향 그래프) """
        self.graph[u][v] = 1
        if not directed:
            self.graph[v][u] = 1  # 무방향 그래프라면 반대 방향도 추가

    def print_graph(self):
        """ 그래프 출력 """
        for row in self.graph:
            print(row)

# 예제 그래프 생성
g_matrix = GraphMatrix(5)
g_matrix.add_edge(0, 1)
g_matrix.add_edge(0, 2)
g_matrix.add_edge(1, 3)
g_matrix.add_edge(2, 3)
g_matrix.add_edge(3, 4)

print("\n인접 행렬 방식 그래프:")
g_matrix.print_graph()