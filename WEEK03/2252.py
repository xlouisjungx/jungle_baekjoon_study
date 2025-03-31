# ----- 선언 부분 -----
from collections import deque

def sort_dfs(graph, in_degree, N):
    queue = deque([node for node in range(1, N+1) if in_degree[node] == 0]) # 진입 차수 0인 노드들
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for i in graph[node]:
            in_degree[i] -= 1 # 간선 제거
            if in_degree[i] == 0:
                queue.append(i) # 새로 진입 차수 0인 노드 추가

    return result if len(result) == N else [] # 사이클 존재하면 실패


# ----- 해결 부분 -----

# 첫째 줄에 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)이 주어진다. M은 키를 비교한 횟수이다. 
# 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1) # 노트별 진입 차수 저장 리스트

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1 # B의 진입 차수 증가

result = sort_dfs(graph, in_degree, N)

print(*result)