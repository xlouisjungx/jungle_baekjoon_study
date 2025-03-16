# ----- 선언 부분 -----
num = int(input())
numL = []

# ----- 문제 해결 부분 -----
for i in range(num):
    numN = int(input())
    numL.append(numN)

numL.sort()

for i in range(num):
    print(numL[i])