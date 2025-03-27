'''
# ----- 선언 부분 -----
import heapq

# 힙 정렬
def HeapSort(numL):
    h = []
    res = []

    for i in numL:
        heapq.heappush(h, i)

    for i in range(len(h)):
        res.append(heapq.heappop(h))

    return res


N = int(input())
numL = []
numLS = []
result = []

# ----- 문제 해결 부분 -----
for i in range(N):
    num = int(input())
    numL.append(num)
    
    numLS = HeapSort(numL)

    if len(numLS) % 2 == 0: # 리스트의 개수가 짝수일때

        num1 = numLS[(len(numLS) // 2) - 1] # 짝수일 때 중간값
        num2 = numLS[(len(numLS) // 2)] # 짝수일 때 중간값의 다음값
        
        if num1 > num2:
            result.append(num2)

        else:
            result.append(num1)

    if len(numLS) % 2 != 0: # 리스트의 개수가 홀수 일떄
        result.append(numLS[len(numLS) // 2]) # 중간값

for i in range(len(result)):
    print(result[i])

# 시간 초과 문제 발생

# 매번 numL.sort() 호출 떄문이라고 함.
# --> 힙정렬 구현 --> 똑같이 함수를 쓰는 부분 떄문에 시간초과

'''

import sys
import heapq

N = int(input())
input = sys.stdin.readline



max_heap = []
min_heap = []
result = []

for _ in range(N):
    num = int(input().strip())

    # 맥스 힙으로 값을 넣기
    heapq.heappush(max_heap, -num)

    # 맥스힙의 값이 더 클때, 최소힙의 최솟값이랑 바꿈
    if min_heap and -max_heap[0] > min_heap[0]:
        val = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, val)

    # 두 리스트 길이 맞추기
    if len(max_heap) > len(min_heap) + 1:
        val = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, val)

    # 두 리스트 길이 맞추기
    elif len(min_heap) > len(max_heap):
        val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -val)
 
    result.append(-max_heap[0])

sys.stdout.write('\n'.join(map(str, result)) + '\n')