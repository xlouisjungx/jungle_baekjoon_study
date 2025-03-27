# ----- 선언 부분 -----
left = 0
right = 0
mid = 0
result = []

def find_liquids(liquids):

    liquids.sort()
    
    left = 0
    right = len(liquids) - 1
    close = float('inf')
    answer = (0, 0)
    
    while left < right:
        mid = liquids[left] + liquids[right]
        
        if abs(mid) < close:
            close = abs(mid)
            answer = (liquids[left], liquids[right])
        
        if mid < 0:
            left += 1
        else:
            right -= 1
    
    return answer

# ----- 문제 해결 부분 -----
N = int(input())
liquids = list(map(int, input().split()))

result = find_liquids(liquids)
print(result[0], result[1])