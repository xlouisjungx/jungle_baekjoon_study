# ----- 선언 부분 -----
T = int(input())
result = []

# ----- 문제 해결 부분 -----
for i in range(T):
    num, String = list(map(str, input().split()))

    for j in range(len(String)):
        result.append(String[j] * int(num))

    result.append("\n")
    
print("".join(result))