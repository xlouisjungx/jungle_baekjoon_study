# ----- 선언 부분 -----
N = int(input())
numL = []

# ----- 문제 해결 부분 -----
numL = list(map(int, input().split()))

numL.sort()

print(numL[0], numL[len(numL)-1])
