# ----- 선언 부분 -----
num = int(input())
numL = []

def SortNum(num: int):
    return

# ----- 문제 해결 부분 -----
for i in range(num):
    numN = int(input())
    numL.append(numN)

numL.sort()

for i in range(num):
    print(numL[i])

# 시간 초과 문제 해결하기