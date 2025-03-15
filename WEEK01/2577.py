# ----- 선언 부분 -----
A = int(input())
B = int(input())
C = int(input())

num = []
result = []

# ----- 문제 해결 부분 -----    
total = A * B * C

num = list(str(total))

for i in range(10):
    cntN = 0
    for j in range(len(num)):
        if str(i) == num[j]:
            cntN = cntN + 1
    result.append(cntN)

for j in range(10):
    print(result[j])
