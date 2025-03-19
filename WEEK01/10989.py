# ----- 선언 부분 -----
from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
    n = len(a)           # 정렬할 배열 a
    f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
    b = [0] * n          # 작업용 배열 b

    for i in range(n):              f[a[i]] += 1                     
    for i in range(1, max + 1):     f[i] += f[i - 1]                 
    for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  
    for i in range(n):              a[i] = b[i]                      

def counting_sort(a: MutableSequence) -> None:
    """도수 정렬"""
    fsort(a, max(a))

# ----- 문제 해결 부분 -----
num = int(input())
numL = [None] * num

for i in range(num):
    while True:
        numL[i] = int(input())
        if numL[i] >= 0: 
            break

counting_sort(numL) 

for i in range(num):
    print(numL[i])