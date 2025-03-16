# ----- 선언 구간 -----
val = list(map(int, input().split()))
H = 0
day = 0

# ----- 문제 해결 구간 -----
while H < val[2]:
    if H + val[0] > val[2]:
        day = day + 1
        break
    else:
        H = H + val[0] - val[1]

print(day)