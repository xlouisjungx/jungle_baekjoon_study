# ----- 선언 부분 -----
T = int(input())
numL = []
result = []

# ----- 문제 해결 부분 -----
for i in range(T):
    numL = list(map(str, input()))
    result.append(numL[0])
    result.append(numL[len(numL)-1])

for i in range(0, len(result), 2):
    print(result[i] + result[i+1])