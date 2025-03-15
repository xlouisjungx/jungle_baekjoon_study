# ----- 선언 구간 -----
def Factorial(a: int):
    total = 1
    for i in range(1, a+1):
        if a == 0:
            total = 1
        else:
            total = total * i

    return total
# ----- 문제 해결 구간 -----
num = int(input())
print(Factorial(num))