# ----- 선언 부분 -----
num = int(input())
num2 = []
ran = 0

# ----- 문제 해결 부분 -----
for i in range(int(num)):
    ran, num2 = input().split()
    ran = int(ran)

    result = ""
    for j in num2:
        result = result + j * ran
    print(result)