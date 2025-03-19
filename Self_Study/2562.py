# ----- 선언 부분 -----
N = 9
numL = []
max = 0
maxH = 0

# ----- 문제 해결 부분 -----
for i in range(N):
    num = int(input())
    numL.append(num)

for i in range(N):
    if numL[i] > max:
        max = numL[i]
        maxH = i + 1

print(max)
print(maxH)