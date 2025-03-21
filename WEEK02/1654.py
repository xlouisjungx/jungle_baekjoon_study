# ----- 선언 부분 -----
def SolveLen(numL: list, K: int, N: int):
    start = 1
    end = 0
    end = max(numL)
    cnt = 0
    MaxR = 0
        
    while start <= end:

        mid = (start + end) // 2
        cnt = 0
        
        for i in range(K):
            cnt += (numL[i] // mid)

        if cnt >= N:
            MaxL = mid
            start = mid + 1    
        else:
            end = mid - 1
    
    return MaxL

K, N = list(map(int, input().split()))
numL = []

# ----- 문제 해결 부분 -----
for i in range(K):
    num = int(input())
    numL.append(num)

print(SolveLen(numL, K, N))