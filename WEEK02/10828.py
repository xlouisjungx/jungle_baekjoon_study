# ----- 선언 부분 -----
N = int(input())
stack = []
result = []

# ----- 문제 헤결 부분 -----
for i in range(N):
    M = list(map(str, input().split()))
    
    if "push" in M:
        stack.append(M[-1])

    if "pop" in M:
        if len(stack) == 0:
            result.append(-1)
        else:
            cnt = stack.pop()
            result.append(cnt)

    if "size" in M:
        result.append(len(stack))
    
    if "empty" in M:
        if len(stack) == 0:
            result.append(1)
        else :
            result.append(0)

    if "top" in M:
        if len(stack) == 0:
            result.append(-1)
        else :
            result.append(stack[-1])

for i in range(len(result)):
    print(result[i])