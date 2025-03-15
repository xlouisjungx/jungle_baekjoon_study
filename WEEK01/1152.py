# ----- 선언 구간 -----
scent = input().split()
cnt = 0
# ----- 문제 해결 구간 -----
for i in scent:
    if i != " ":
        cnt += 1
print(cnt)