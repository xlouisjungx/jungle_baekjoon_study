# 실버 5 문제

import sys
sys.setrecursionlimit(10**6)

num = 1

def Find_Num(S, num):
    total = 0
    
    # 합 공식
    total = num * (num + 1) // 2

    if total == S:
        return num
    
    elif total > S:
        return num -1
    
    else:
        return Find_Num(S, num + 1)

S = int(sys.stdin.readline())
print(Find_Num(S, num))