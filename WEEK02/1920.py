# ----- 선언 부분 -----
result = []

# ----- 문제 해결 부분 -----
N = int(input())
numL = set(map(int, input().split())) # set을 활용하여 시간 초과문제를 해결

comN = int(input())
comNL = list(map(int, input().split()))

for i in range(comN):
    if comNL[i] in numL:
        result.append(1)
    else:
        result.append(0)

for i in range(comN):
    print(result[i])

# set이란?
# 파이썬의 집합 자료형이다. 중복된 값을 허용하지 않고, 값의 존재 여부를 아주 빠르게 확인할 수 있다.
# 중복방지: 같은 값을 여러 번 넣어도 한번만 저장된다.
# 순서 없음: 리스트처러 인덱스로 접근할 수 없다.
# 탐색 속도 빠름: 값이 있는지 확인할 때 O(1)의 시간 복잡도를 가진다.