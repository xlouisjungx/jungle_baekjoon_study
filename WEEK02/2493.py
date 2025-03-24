# ----- 선언 부분 -----
N = int(input())
numL = list(map(int, input().split()))
stack = []
result = [0] * N

# 예제
# 5
# 6 9 5 7 4

# 0 0 2 2 4

# ----- 문제 해결 부분 -----
for i in range(N):
    while stack and numL[stack[-1]] <= numL[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1] + 1

    stack.append(i)

print(*result)