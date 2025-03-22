# ----- 선언 부분 -----
K = int(input())
N = 0
numL = []
result = 0

# ----- 문제 해결 부분 -----
for i in range(K):
    N = int(input())
    if N > 0:
        numL.append(N)

    if N == 0:
        numL.pop()

for i in range(len(numL)):
    result += numL[i]

print(result)