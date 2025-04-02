# ----- 선언 부분 -----
import heapq

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

INF = int(1e9)
distance = [INF] * (N+1)

# ----- 해결 부분 -----

# 인접 리스트
graph = [[] for _ in range(N+1)] # 그래프 초기화
# x번 도시에 갈 수 있는 도시들의 리스트 (도착 도시, 비용) 저장

for i in range(M):
    a, b, c = map(int, input().split()) # a번 도시에서 b번 도시로 가는 비용이 c인 경로를 저장
    graph[a].append((b, c))

q = [] # 우선순위 큐 역할을 하는 리스트

start, end = map(int, input().split()) # 출발 도시와 도착 도시를 입력
heapq.heappush(q, (0, start))   # 우선순위 큐에 (거리, 노드) 형식으로 push 
# (처음 시작 도시는 거리 0으로 설정하여 큐에 넣음)

while q:
    dist, now = heapq.heappop(q) # 가장 작은 비용을 가진 노드를 꺼냄
    # 각각 현재 노드까지의 거리, 현재 탐색 중인 노드를 담당

    if distance[now] < dist: # 이미 처리된 노드면 패스한다. (더 짧은 경로롤 방문한 적 있다는 말이 되는 것.)
        continue

    for node, cost in graph[now]: # 현재 노드(now)에서 이동할 수 있는 모든 연결된 노드(node) 확인
        
        # 기존에 알고 있던 distance[node]보다 현재 경로 (cost _ dist)가 더 짧으면 갱신
        # 갱신된 정보로 우선순위 큐에 (새 거리, 노드) 삽입
        if distance[node] > cost + dist:
            distance[node] = cost+dist
            heapq.heappush(q, (cost+dist, node))

print(distance[end]) # 출력