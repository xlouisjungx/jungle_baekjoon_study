# ----- 선언 부분 -----
from itertools import permutations

num = int(input())
numL = []
#numN = 0

maxV = 0

def FindAllArray(numL, perm, used):
    global maxV # 전역 변수를 사용할 때 사용한다.

    if len(perm) == len(numL):
        total = 0
        
        for i in range(len(perm)-1):
            total += abs(perm[i] - perm[i+1]) # abs : 순열의 두 인덱스를 사용해 차이를 계산해줌.
        maxV = max(maxV, total) # 최댓값 알려줌
        return

    # 배열의 각 원소를 한 번씩 사용
    for i in range(len(numL)):
        if not used[i]:  # 사용되지 않은 원소라면 선택
            used[i] = True
            FindAllArray(numL, perm + [numL[i]], used)  # 다음 단계로
            used[i] = False  # 백트래킹: 사용한 원소를 되돌림
        
    
# ----- 문제 해결 부분 -----
numL = list(map(int, input().split()))

used = [False] * num  # 각 원소의 사용 여부를 추적
FindAllArray(numL, [], used)
print(maxV)

#for p in permutations(numL): # numL의 가능한 순열을 생성하는 함수이며, 그 순열들을 하나씩 반환한다. 그것을 p가 담당한다.
    #total = 0

    #for i in range(num-1):
        #total += abs(p[i] - p[i+1]) # abs : 순열의 두 인덱스를 사용해 차이를 계산해줌.
        #maxV = max(maxV, total) # 최댓값 알려줌

#print(maxV)
