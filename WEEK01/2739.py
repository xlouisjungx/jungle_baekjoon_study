# ----- 선언 부분 -----
num = int(input())

# ----- 문제 해결 부분 -----
for i in range(1,10):
    for j in range(num, num+1):
        print(j, end=" ")
        print("*", end=" ")
        print(i, end=" ")
        print("=", end=" ")
        print(j*i)