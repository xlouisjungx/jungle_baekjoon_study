import sys

result = []

def Bunnies(num):
    if num <= 1:
        result.append(1)
        return
    
    F = [0] * (num + 1)
    F[0] = 1
    F[1] = 1

    for i in range(2, num+1):
        F[i] = F[i-1] + F[i-2]

    result.append(F[-1])
    return

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline().strip())
    Bunnies(num)

for i in range(len(result)):
    print(result[i])