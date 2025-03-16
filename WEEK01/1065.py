# ----- 선언 부분 -----
num = int(input())
numst = str(num)
cnt = 0

def is_hansu(num: int):
    cnt = 0
    if num < 100:
        return 1
    elif num >= 100:
        numL = list(map(int, str(num)))
        numD = numL[1] - numL[0] # 둘째 자리 - 첫쨰자리 = 첫 차이 값
        for i in range(1, len(numL)-1):
            if  numL[i+1] - numL[i] == numD:
                cnt += 1
        return cnt
    
# ----- 문제 해결 부분 -----
for i in range(1, num+1):
    cnt += is_hansu(i)


print(cnt)