# 브론즈 3 문제

# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.
# A는 300초, B는 60초, C는 10초

import sys

def Min_Control(T):

    A = 300
    B = 60
    C = 10

    Min_A = T // A
    T %= A

    Min_B = T // B
    T %= B

    Min_C = T // C
    T %= C

    if T != 0:
        print("-1")
    
    else:
        print(Min_A, end=" ")
        print(Min_B, end=" ")
        print(Min_C)

T = int(sys.stdin.readline())
Min_Control(T)

# Wa! 100점!