# 문제를 이해하고, 방법을 공부하기 위해 참고한 강의 링크 : http://youtube.com/watch?v=c38slnsLRk4

import random

# ----- 선언 구간 -----
numL = []
n1 = 0
n2 = 0
numS = []

def FindS():
    num = sum(numL) - 100 # 찾아야할 숫자 계산
    for i in range(0, 8):
        for j in range(i+1, 9): # N개중에서 2개를 뽑는 모든 조합
            if numL[i] + numL[j] == num:
                return numL[i], numL[j]
            
# ----- 문제 해결 구간 -----
for i in range(9):
    numN = int(input())
    numL.append(numN)

n1, n2 = FindS()
numS = sorted(numL)

for i in numS:
    if i != n1 and i != n2:
        print(i)