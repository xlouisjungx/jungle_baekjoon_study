# ----- 선언 부분 -----
n = int(input())

def Pibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return Pibonachi(n-1) + Pibonachi(n-2)

# ----- 문제 해결 부분 -----
print(Pibonachi(n))