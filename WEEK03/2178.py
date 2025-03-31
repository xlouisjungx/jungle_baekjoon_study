# ----- 선언 부분 -----
from collections import deque
import sys

def bfs(graph, N, M):
    # 상, 하, 좌, 우 이동 (dx, dy)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0)])  # 시작점 (0,0)에서 BFS 시작

    while queue:
        x, y = queue.popleft()

        # 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위를 벗어나지 않고, 이동 가능한 경우
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 거리 업데이트
                queue.append((nx, ny))

    return graph[N-1][M-1]

# ----- 문제 해결 부분 -----
N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

print(bfs(graph, N, M))