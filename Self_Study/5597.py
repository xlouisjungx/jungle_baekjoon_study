# ----- 선언 부분 -----
N = 28

numST = []
numLR = []

# ----- 문제 해결 부분 -----
for i in range(N):
    num = int(input())
    numLR.append(num)

numLR.sort()      

for i in range(N-1):
    if numLR[i+1] - numLR[i] != 1:
        numST.append(numLR[i]+1)

for i in range(len(numST)):
    print(numST[i])