# ----- 선언 부분 -----
T = int(input())
n1 = 0
n2 = 0
R = 0
result = []

# ----- 문제 해결 부분 -----
for i in range(T):
    n = int(input())
    
    for j in range(3, n):
        if j % 2 != 0:
            n1 = j
            n2 = n - n1
            if n1 > n2:
                n1, n2 = n2, n1
        if j/2 >= n1 and n2 >= j/2:
            if (j+2)/2 == n1 or n2 == (j+2)/2:
                continue
            else:
                break
    result.append(n1)
    result.append(n2)


print(result)