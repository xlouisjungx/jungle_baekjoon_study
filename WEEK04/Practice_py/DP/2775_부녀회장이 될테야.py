# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 
# 사람들을 데려와 살아야 한다

T = int(input()) # 테스트 케이스 수

result = []
room = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    room[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        room[i][j] = room[i-1][j] + room[i][j-1]

for i in range(T):
    k = int(input()) # 층
    n = int(input()) # 호실
    result.append(room[k][n])

for i in range(T):
    print(result[i])