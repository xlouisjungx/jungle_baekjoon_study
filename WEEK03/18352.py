# ----- 선언 부분 -----
from collections import deque
import sys

def bfs(graph, start, visited):

    
    queue = deque([start]) # 시작 도시를 설정
    visited[start] = 0 # 거리 0

    while queue:
        node = queue.popleft() # 현재 방문 노드
        for i in graph[node]: # node와 연결된 다른 노트들
            if visited[i] == -1: # 노드를 아직 방문하지 않았을 시,
                visited[i] = visited[node] + 1 # 거리측정
                # 출발 노드(X)에서 i번 노드까지의 거리 = 현재 node에서 i번 노드로 이동하므로, 거리가 +1 증가
                queue.append(i)

# ----- 해결 부분 -----

# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N + 1)

cnt = 0

# N은 "도시(노드) 개수"
# 문제에서 주어진 N은 도시(노드)의 개수를 의미.
# graph[a].append(b)처럼 사용하려면, graph의 크기가 최소한 N까지 존재해야 함.
# 파이썬에서 리스트의 인덱스는 0부터 시작하므로, 노드 번호(1~N)에 맞추기 위해 N+1 크기로 리스트를 생성.

# 그렇다면 M은 왜 안되는가?
# 👉 M은 "도로(간선) 개수"를 의미할 뿐, 노드 개수와 관계가 없음.
# 👉 graph는 노드 중심의 인접 리스트 형태로 만들어야 하므로, 노드 개수 N을 기준으로 초기화해야 함.

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


bfs(graph, X, visited)

for i in range(N+1):
    if visited[i] == K: # 거리가 K이면,
        print(i) # 출력
        cnt += 1 # 있다면 더함

if cnt == 0: # 그 cnt의 값이 없다면
    print(-1)