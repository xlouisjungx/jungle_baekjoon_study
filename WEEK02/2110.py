# ----- 선언 부분 -----
N, C = map(int, input().split())
numL = []
start = 0
end = 0
total = 0
mid = 0
result = 0
# ----- 문제 해결 부분 -----
for i in range(N):
    num = input()
    
    numL.append(num)

numL.sort()

while start <= end:
    
    total = 0
    mid = (start + end) // 2

    if 집간의 거리가 >= 1:
        total = 현재 위치 - 다른집위치 # 최솟 값 찾기
        if result > total:
            result = total
        start = mid + 1


    else:
        end = mid - 1

print(result)

print(*numL)