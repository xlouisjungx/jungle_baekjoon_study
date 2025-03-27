f = open("input.txt", "r")
g = int(f.readline())
graph = [[0 for _ in range(g)] for _ in range(g)]
stack = []
visited = [False for _ in range(g)]
answer = []

while True :
    v = list(map(int, f.readline().split()))
    if not v :
        break
    graph[v[0]][v[1]] = 1
    graph[v[1]][v[0]] = 1

def dfs(n) :
    
    stack.append(n)
    
    while len(answer) != g :
        v = stack.pop()
        visited[v] = True
        answer.append(v + 1)
        
        for i in range(g-1, -1, -1) :
            if graph[v][i] and not visited[i] :
                stack.append(i)
    print(*answer)

dfs(0)

# 재귀함수를 이용한 DFS 구현
'''
# 윗부분 동일

def dfs(n) :
    print(n + 1, end =" ")
    visited[n] = True
    for i in range(g) :
        if graph[n][i] and not visited[i] :
            dfs(i)

dfs(0)
'''
