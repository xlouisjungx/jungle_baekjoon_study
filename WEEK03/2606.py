# ----- 선언 부분 -----
import sys

num1 = int(input())
num2 = int(input())

def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)  # 방문 처리
        #print(node, end=" ")  # 방문한 노드 출력
        for neighbor in graph[node]:  # 인접 노드 방문
            dfs_recursive(graph, neighbor, visited)

    return len(visited) - 1
    
# ----- 문제 해결 부분 -----
graph = {i: [] for i in range(1, num1 + 1)}

for i in range(1, num2+1):
    A, B = map(int, sys.stdin.readline().split())

    graph[A].append(B)
    graph[B].append(A)

visited = set()
print(dfs_recursive(graph, 1, visited))