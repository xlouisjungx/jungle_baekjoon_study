# ----- 선언 부분 -----
num = int(input())
result = []
above_avg = 0
# ----- 문제 해결 부분 -----

for _ in range(num):

    score = list(map(int, input().split()))
    
    stu = 0
    scores = 0
    avr = 0
    above_avg = 0
    
    stu = score[0]
    scores = score[1:]

    avr = sum(scores) / stu

    for score in scores:
        if score > avr:  # 평균보다 크면
            above_avg = above_avg + 1  # 1 증가

    total = (above_avg / stu) * 100
    result.append(total)

for i in range(num):
    print(f"{result[i]:.3f}%")