# ----- 선언 구간 -----
num = int(input())
A = []
B = []
result = []

# ----- 문제 해결 구간 -----

for i in range(0,num):
    numA, numB = map(int, input().split())
    
    A.append(numA)
    B.append(numB)

    result.append(A[i] + B[i])

for i in range(0,num):
    print(result[i])