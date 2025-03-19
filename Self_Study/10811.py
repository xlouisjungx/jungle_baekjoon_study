# ----- 선언 부분 -----
N, M = list(map(int, input().split()))

numL = []
numLR = []
# ----- 문제 해결 부분 -----

for i in range(N):
    numL.append(i+1)

for x in range(M):
    i, j = list(map(int, input().split()))
    numL[i-1:j] = numL[i-1:j][::-1] # 입력받은 부분을 뒤집기
    
print(*numL)