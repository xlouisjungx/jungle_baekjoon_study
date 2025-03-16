import math
def is_prime(num: int):
    if num <= 1:
        return False
    if num == 2:  # 2는 소수
        return True
    if num % 2 == 0:  # 짝수는 소수가 아님
        return False
    for j in range(3, int(math.sqrt(num)) + 1, 2):  # 3부터 sqrt(num)까지 홀수로만 나누기
        if num % j == 0:
            return False
    return True

# ----- 선언 부분 -----
T = int(input())
result = []

# ----- 문제 해결 부분 -----
for i in range(T):
    n = int(input())
    
    n1 = n // 2
    n2 = n // 2

    for j in range(3, n):
        if is_prime(n1) and is_prime(n2):
            result.append((n1, n2))
            break
        else:
            n1 = n1 - 1  
            n2 = n2 + 1 

for i in range(len(result)):
    print(result[i][0], result[i][1])