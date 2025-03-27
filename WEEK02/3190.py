# 강의와 GPT를 이용하여 해결

# ----- 선언 부분 -----
N = int(input()) # 보드의 크기
K = int(input()) # 사과의 위치

location = []
way = []

cnt = 0 # 시간 측정

# ----- 문제 해결 부분 -----

# 사과의 위치 첫 번쨰 정수는 행(가로), 두 번째 정수는 열(세로) 위치
location = [tuple(map(int, input().split())) for _ in range(K)]

L = int(input()) # 뱀의 방향 변환 횟수

# X초가 지나면 C의 방향따라 회전
way = [input().split() for _ in range(L)]

way1 = [-1, 0, 1, 0]
way2 = [0, 1, 0, -1] # 시계방향으로 방향정의

waytbl = [0] * (10001) # 방향전환에 사용되는 공간

for sec, turn in way:
    waytbl[int(sec)] = turn

right = 1 # 오른쪽
snake = [(1,1)] # 뱀

while True:
    cnt += 1

    headX, headY = snake[0]

    nX = headX + way1[right]
    nY = headY + way2[right] # 진행 방향으로 한칸 이동

    # 벽에 부딪히거나 몸에 부딪혔을 때
    if 1 <= nX <= N and 1 <= nY <= N and (nX, nY) not in snake:
        
        snake.insert(0, (nX, nY)) # 이동좌표 확장
        
        if (nX, nY) in location:
            location.remove((nX, nY))
        else:
            snake.remove((snake[-1])) # 꼬리 제거

        # 방향전환
        if waytbl[cnt] == 'D':
            right = (right+1) % 4
        elif waytbl[cnt] == 'L':
                right = (right + 3) % 4

    else:   # 부딪혀서 종료되는 경우
        break

print(cnt)