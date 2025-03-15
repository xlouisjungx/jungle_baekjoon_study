import math
# ----- 선언 부분 -----
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

    '''
    if num > 2:
        for j in range(2, num-1):
            if num % j != 0:
                return True
            else:
                return False
    if num == 2:
        return True
            
    if num <= 1:
        return False
    
    return True
    '''

# ----- 문제 해결 부분 -----
num = int(input())
numR = list(map(int, input().split()))

cnt = 0

for i in numR:
    if is_prime(i):
        cnt = cnt + 1

print(cnt)