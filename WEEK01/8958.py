# ----- 선언 부분 -----
num = int(input())
Q = []
result = []

score = 0
plus = 1

scoreL = []

# ----- 문제 해결 부분 -----
for i in range(num):
    Q = input()
    score = 0
    plus = 1
    for j in range(len(Q)):
        if Q[j] == "O":
            score = score + plus
            plus = plus + 1
        elif Q[j] == "X":
            plus = 1
    result.append(score)

for i in range(num):
    print(result[i])