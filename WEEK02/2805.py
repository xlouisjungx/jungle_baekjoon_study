# ----- 선언 부분 -----

# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
# N M --> 각각 나무의 수, 집에 가져가려는 나무의 길이
# 4 7
# 20 15 10 17
# 15 15 10 15
#  5  0  0  2 --> 7

# 5 20
#  4 42 40 26 46
# 36 36 36 36 36
#  0  6  4  0 10 --> 20

N, M = map(int, input().split())
Trees = []
total = 0

start = 0
Hight = 0

# ----- 문제 해결 부분 -----
Trees = list(map(int, input().split()))

Hight = max(Trees) // 2

while total != M:
    total = 0
    for i in range(N):
        if Trees[i] - Hight < 0 or Trees[i] - Hight == 0:
            total += 0
        if Trees[i] - Hight > 0:
            total += Trees[i] - Hight

    Hight += 1

print(Hight-1)