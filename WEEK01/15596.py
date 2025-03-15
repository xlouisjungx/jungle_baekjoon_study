# ----- 선언하는 부분 -----
def solve(a: list) -> int:
    result = 0
    for i in a:
        result = result + i
    return result

# ----- 문제 해결 부분 -----
num = []

num = list(map(int, input().split()))

print(solve(num))