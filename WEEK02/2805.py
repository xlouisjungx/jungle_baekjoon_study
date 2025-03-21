# ----- 선언 부분 -----

# 이분 탐색: 중간값을 찾고, 찾을려는 수보다 크면 +1, 작으면 -1

# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

import sys

def FindWood(Trees: list, M):
    
    Trees.sort()

    start = 0
    end = Trees[-1]
    MaxL = 0
    
    

    while start <= end:
        
        mid = (start + end) // 2
        total = 0

        for i in Trees:
            if i > mid:
                total += i - mid

        if total < M:
            end = mid - 1
        
        # 이쪽 조건문을 바꾸었더니 통과함...왜 일까 좀 찝찝하다(몰라서 그런듯?)

        # 처음에는 if total > M 으로 했었는데, 이때 오류가 시간초과였고, 지피티 말로는 너무 모든 경우를 계산하려고 해서,
        # 시간 초과 오류가 나온다고 함.  

        # 이분탐색은 중간값을 찾고, 비교하여 범위를 다시 설정해서 비교하는 방식이라고 이해했는데.... 
        # 조건문에서 더 작을때만 봐주고, 나머지는 다 else처리해서 경우의 수가 줄었나? 라는 생각이 든다
        # 팀원이 알려준 파라메트릭 서치를 안써서 더 찝찝한거 같기도 합니다.


        else:
            MaxL = mid
            start = mid + 1


    return MaxL

N, M = map(int, sys.stdin.readline().split())


# ----- 문제 해결 부분 -----
Trees = list(map(int, sys.stdin.readline().split()))
print(FindWood(Trees, M))