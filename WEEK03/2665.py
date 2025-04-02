# 블로그 코드 / 다시 풀 예정

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(n, grid):
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    dq = deque([[0, 0]])

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx  < n and 0 <= ny < n:
                if grid[nx][ny] == '1' and dist[nx][ny] > dist[x][y]:
                    dist[nx][ny] = dist[x][y]
                    dq.appendleft((nx, ny))

                elif grid[nx][ny] == '0' and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))

    return dist[n-1][n-1]


n = int(input())
grid = [input().strip() for _ in range(n)]

print(bfs(n, grid))