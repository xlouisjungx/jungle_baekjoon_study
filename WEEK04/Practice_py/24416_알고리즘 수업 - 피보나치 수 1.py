import sys
sys.setrecursionlimit(10**6)

result = []

# 재귀 / fib(n)이 재귀적으로 호출되는데, 피보나치 수열의 값이 코드1(재귀 호출)의 실행 횟수와 같다.
# 메모이제이션 (Top-down 방식, 재귀 + 캐싱)

# fib(5)
# ├── fib(4)
# │    ├── fib(3)
# │    │    ├── fib(2) → 1 (기저 조건)  
# │    │    ├── fib(1) → 1 (기저 조건)  
# │    │    └── 결과: 1 + 1 = 2  
# │    ├── fib(2) → 1 (기저 조건)  
# │    └── 결과: 2 + 1 = 3  
# ├── fib(3) (이미 계산됨) → 2  
# └── 결과: 3 + 2 = 5

# 재귀적으로 fib(n-1)과 fib(n-2)를 호출하므로,
# 재귀 호출의 총 실행 횟수가 피보나치 수열의 값과 일치하게 됨.

# 결론
# ✅ 재귀적으로 fib(n-1) + fib(n-2)를 호출하면서, 실행 횟수가 피보나치 수열의 값과 같아짐.
# ✅ 따라서 dp[n]을 반환하면 피보나치 값이 나오는데, 그 값이 곧 재귀 호출 횟수!

dp = [-1] * 50 # 충분하게 크기 설정
def fib(n):

    if n == 1 or n == 2:
        return 1;  # 코드1

    if dp[n] != -1: # 이미 계산한 값이면 바로 반환
        return dp[n]
    
    dp[n] = (fib(n - 1) + fib(n - 2))
    return dp[n]

# 동적 프로그래밍
def fibonacci(n):
    
    cnt = 0

    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1

    f = [0] * (n+1)

    f[1] = 1
    f[2] = 1

    for i in range(3, n+1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2];  # 코드2
        
    return cnt

n = int(sys.stdin.readline().strip())


result.append(fib(n))
result.append(fibonacci(n))

print(*result)