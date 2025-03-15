# ----- 선언 구간 -----
num = input().split()
result = []

# ----- 문제 해결 구간 -----

# 리스트안에 있는 숫자 뒤집는 방법
for i in num:
    numR = int(i[::-1]) # 각 숫자를 뒤집고, int로 변환
    result.append(numR)

print(max(result))