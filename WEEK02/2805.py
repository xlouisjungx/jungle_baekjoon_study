# ----- 선언 부분 -----

# 이분 탐색: 중간값을 찾고, 찾을려는 수보다 크면 +1, 작으면 -1

# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

import sys

def FindWood(Trees: list, N, M):
    
    Trees.sort()

    start = 0
    end = Trees[-1]
    MaxL = 0
    
    

    while start <= end:
        
        mid = (start + end) // 2
        total = 0
        
        # 차이값의 합
        for i in Trees:
            if i > mid:
                total += i - mid

        if total >= M:
            MaxL = mid
            start = mid + 1

        else:
            end = mid - 1


    return MaxL

N, M = map(int, sys.stdin.readline().split())


# ----- 문제 해결 부분 -----
Trees = list(map(int, sys.stdin.readline().split()))
print(FindWood(Trees, N, M))