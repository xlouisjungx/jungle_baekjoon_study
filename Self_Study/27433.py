# ----- 선언 부분 -----
def Factorial(num):
    if num < 1:
        return 1
    
    return num * Factorial(num-1)

# ----- 문제 해결 부분 -----
num = int(input())
print(Factorial(num))