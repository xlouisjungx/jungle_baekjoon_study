# ----- 선언 부분 -----
num = input()
num2 = []
result = []

# ----- 문제 해결 부분 -----
for i in range(int(num)):
    num2 = list(map(str, input().split()))
    
    num3 = list(num2[1])
    num4 = int(num[0])

print(num2)
print(num3)
print(num4)