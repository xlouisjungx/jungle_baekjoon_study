# Velog 참고해서 품

# ----- 선언 부분 -----
white = 0
blue = 0

Rnum = []

def Cut_White_blue(sero, garo, N):
    
    global white, blue

    color = Rnum[sero][garo] 

    for i in range(sero, sero + N): # 현재 종이 조각의 모든 행
        for j in range(garo, garo + N): # 모든 종이 조각의 모든 열
            if color != Rnum[i][j]:
                Cut_White_blue(sero, garo, N // 2) # 1 사분면
                Cut_White_blue(sero, garo + N // 2, N // 2) # 2 사분면
                Cut_White_blue(sero + N // 2, garo, N // 2) # 3 사분면
                Cut_White_blue(sero + N // 2, garo + N // 2, N // 2) # 4 사분면
                return
            
    if color == 0:
        white += 1
    
    else:
        blue += 1

# ----- 문제 해결 부분 -----
N = int(input()) # 색종이 넓이
for i in range(N):
    Rnum.append(list(map(int, input().split())))

Cut_White_blue(0, 0, N)
print(white)
print(blue)