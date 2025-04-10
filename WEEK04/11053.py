# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성

import sys

cnt = 0
Max_cnt = 0
Compare_Num = 0
result = []

# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
N = int(sys.stdin.readline().strip())

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
A = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N):
    cnt = 0
    Compare_Num = A[i]
    for j in range(i):
        num = max(Compare_Num, A[j])
        result.append

        if Max_cnt < cnt:
            Max_cnt = cnt

print(Max_cnt+1)