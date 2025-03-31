# ----- 선언 부분 -----
import sys
sys.setrecursionlimit(10**6) # 한도설정

def dfs(node, pre):
    
    parent[node] = pre

    for i in graph[node]: # 현재 연결된 노드 탐색
        if i == pre: # 방문처리 조건문
            continue
        dfs(i, node) # 자식 노드에 대한 재귀

N = int(input()) # 노드의 개수

graph = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# ----- 해결 부분 -----
dfs(1, 0)

for i in parent[2:]:
    print(i)

# parent 리스트의 역할

# 노드의 부모 노드를 저장하는 용도로 사용.
# 즉, parent[i]는 노드 i의 부모 노드를 저장하는 변수.
# 트리는 방향성이 없고, graph 리스트는 연결 관계만 저장.
# 따라서, parent 리스트가 없으면 각 노드의 부모를 따로 저장할 방법이 없기 떄문에.
# parent를 사용하면, DFS를 통해 부모 노드를 한 번에 기록할 수 있다.