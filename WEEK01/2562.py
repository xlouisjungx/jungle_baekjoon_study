# ----- 선언 구간 -----
NumL1 = []
NumL2 = []
result = 0

# ----- 문제 해결 구간 -----
# 입력 받는 부분
for i in range(1, 10):
    N = int(input())
    NumL1.append(N)
    NumL2.append(N)

# 최댓값 찾는 부분
for i in range(9):
    if result < NumL2[i]:
        result = NumL2[i]

print(result)

# 최댓값 위치 찾는 부분
for i in range(9):
    if result == NumL1[i]:
        print(i+1)