# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
# 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
# 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 

# 1+2+3-4×5÷6 = 1
# 1÷2+3+4-5×6 = 12
# 1+2÷3×4-5+6 = 5
# 1÷2×3-4+5+6 = 7

# 블로그 코드 / 다시 풀 예정

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split())) # 연산자 부호들

max_result = int(-1e9)
min_result = int(1e9)

def calculate(a, b, operator_index):
    if operator_index == 0: # 덧셈
        return a + b
    elif operator_index == 1: # 뺄셈
        return a - b
    elif operator_index == 2: # 곱셈
        return a * b
    elif operator_index == 3: # 나눗셈
        return divide(a, b)

def divide(a, b):
    if a < 0:
        return -(-a // b)
    else:
        return a // b
    
def dfs(index, current_result):
    global max_result, min_result
    if index == N:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1 # 연산자 사용
            next_result = calculate(current_result, A[index], i)
            dfs(index + 1, next_result)
            operators[i] += 1 # 연산자 복구 (백트래킹)

dfs(1, A[0])

# 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력
print(max_result)
print(min_result)