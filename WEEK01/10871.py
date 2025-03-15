# ----- 선언 구간 -----
num, comN = map(int, input().split())
listN = []
result = []

# ----- 문제 해결 구간 -----
listN = list(map(int, input().split()))


for j in range(num):
    if listN[j] < comN:
        result.append(listN[j])

for i in range(len(result)):
    if i < len(result)-1:
        print(result[i], end=" ")
    elif i < len(result):
        print(result[i])