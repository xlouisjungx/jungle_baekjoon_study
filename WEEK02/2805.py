# ----- 선언 부분 -----

# 이분 탐색: 중간값을 찾고, 찾을려는 수보다 크면 +1, 작으면 -1

# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
# N M --> 각각 나무의 수, 집에 가져가려는 나무의 길이
# 4 7
# 20 15 10 17
# 15 15 10 15
#  5  0  0  2 --> 7

# 10
# 10 5 0 7 --> 22

# 11
# 9 4 0 6 --> 19

# 12
# 8 3 8 5 --> 24

# 13
# 7 2 7 4 --> 20

# 14
# 6 1 0 3 --> 10

# 15
# 5 0 0 2 --> 7

# 5 20
#  4 42 40 26 46
# 36 36 36 36 36
#  0  6  4  0 10 --> 20

N, M = map(int, input().split())
Trees = []
total = 0

start = 0
end = 0
MaxL = 0

# ----- 문제 해결 부분 -----
Trees = list(map(int, input().split()))
end = max(Trees)

while start <= end:
    total = 0

    mid = (start + end) // 2

    # 차이값의 합
    for i in range(N):
        if Trees[i] - mid <= 0:
            total += 0
        else:
            total += (Trees[i] - mid)
    print("현재 토탈값: ", total)

    if total >= M:
        MaxL = mid
        start = mid + 1

    else:
        end = mid - 1 
    

print(MaxL)