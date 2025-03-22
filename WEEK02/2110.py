# ----- 선언 부분 -----
def FindMin(numL, mid, N, C):
    
    cnt = 1

    num = numL[0] # 첫 번째 공유기 설치 위치

    for i in range(N):
        if numL[i] - num >= mid: # 기준점 
            cnt += 1
            num = numL[i] # 가장 최근 공유기 설치 위치 업데이트
    if cnt >= C:
        return True

    return False # 계산 시, 아니면

def ParaSearch(numL, N, C):  # 파라메트릭 서치
    
    numL.sort()
    
    start = 0
    end = numL[-1] - numL[0]
    mid = 0
    maxN = 0

    while start <= end:
        
        mid = (start + end) // 2

        if FindMin(numL, mid, N, C):
            start = mid + 1
            maxN = mid
        else:
            end = mid - 1

    return maxN # 최종값


# ----- 문제 해결 부분 -----
N, C = map(int, input().split()) # 집의 개수, 공유기의 개수

numL = [int(input()) for i in range(N)]

print(ParaSearch(numL, N, C))