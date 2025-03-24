# ----- 선언 부분 -----
left = 0
right = 0
mid = 0
result = []

def find_liquids(liquids):
    # 용액들을 정렬
    liquids.sort()
    
    left, right = 0, len(liquids) - 1
    close = float('inf')
    answer = (0, 0)
    
    while left < right:
        mid = liquids[left] + liquids[right]
        
        # 현재 혼합값이 더 0에 가까우면 갱신
        if abs(mid) < close:
            close = abs(mid)
            answer = (liquids[left], liquids[right])
        
        # 혼합값이 0보다 작으면 left 증가, 크면 right 감소
        if mid < 0:
            left += 1
        else:
            right -= 1
    
    return answer

# 입력
n = int(input())
liquids = list(map(int, input().split()))

# 결과 출력 (오름차순 정렬)
result = find_liquids(liquids)
print(result[0], result[1])