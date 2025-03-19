# ----- 선언 부분 -----
N = int(input())
ScoreL = []
total = 0
ScoreM = 0

# ----- 문제 해결 부분 -----
ScoreL = list(map(int, input().split()))
ScoreM = max(ScoreL)

for i in range(len(ScoreL)):
    total += ScoreL[i] / ScoreM * 100

total = total / N

print(total)