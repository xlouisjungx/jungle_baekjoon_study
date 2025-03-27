# ----- 선언 부분 -----
import sys
numL = []

N = int(input())
input = sys.stdin.readline

for i in range(N):
    num = int(input())
    numL.append(num)

numL.sort()

num1 = 


# ----- 문제 해결 부분 -----
sys.stdout.write('\n'.join(map(str, numL)) + '\n')