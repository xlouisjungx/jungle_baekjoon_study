# ----- 선언 부분 -----
T = int(input())
result = []

# ----- 문제 해결 부분 -----
for i in range(T):
    StringL = list(map(str, input()))
    
    stack = []
    vps = True
    
    for j in StringL:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if not stack:
                vps = False
                break
            else:
                stack.pop()

    if vps and not stack:
        result.append("YES")

    else:
        result.append("NO")

for i in range(len(result)):
    print(result[i])