# ----- 선언 부분 -----
N = int(input())
start = 0
end = 0
result = []
comN = 0
minN = 0
sumN = 0

# ----- 문제 해결 부분 -----
numL = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        sumN = numL[i] + numL[j]
        comN = abs(sumN)

        if comN < minN:
            minN = comN

            result.append(numL[i])         
            result.append(numL[j])

result.sort()

print(*result)
    


'''
def brute_force(N, liquids):
    min_diff = float('inf')  # 무한대로 초기화
    best_pair = (0, 0)

    # 모든 용액 쌍을 비교
    for i in range(N):
        for j in range(i+1, N):
            current_sum = liquids[i] + liquids[j]
            current_diff = abs(current_sum)

            if current_diff < min_diff:
                min_diff = current_diff
                best_pair = (liquids[i], liquids[j])
    
    return best_pair

# 입력 받기
N = int(input())
liquids = list(map(int, input().split()))

# brute force로 가장 0에 가까운 두 용액 찾기
result = brute_force(N, liquids)

# 결과 출력 (오름차순으로 출력)
print(*sorted(result))

'''