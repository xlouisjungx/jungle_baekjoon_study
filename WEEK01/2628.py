# ----- 선언 부분 -----
Garo, Sero = list(map(int, input().split()))
N = int(input())

GaroL = [0, Garo]
SeroL = [0, Sero]

# ----- 문제 해결 부분 -----

for _ in range(N):
    Where, How = map(int, input().split())
    
    if Where == 0:  # 가로로 자르기
        SeroL.append(How)
    elif Where == 1:  # 세로로 자르기
        GaroL.append(How)

# ----- 최대 길이 계산 -----
GaroL.sort()
SeroL.sort()

maxGaro = max(GaroL[i+1] - GaroL[i] for i in range(len(GaroL) - 1))
maxSero = max(SeroL[i+1] - SeroL[i] for i in range(len(SeroL) - 1))

# ----- 결과 출력 -----
print(maxGaro * maxSero)

'''

지금 코드는 자른 위치를 추적하는 방법이 잘못됐어요.

자르는 위치는 각 자름마다 끝점에서 잘린 위치까지의 길이를 추적해야 합니다.
하지만, 현재 코드는 첫 번째 자름 위치만 사용하고, 이후 자름은 첫 번째 길이에서 또 빼고 있어요.
→ 이렇게 하면, 여러 번 자를 때 제대로 잘라지지 않습니다.

라고 지피티가 그런다...

if(N == 0):
    SeroL.append(Sero)
    GaroL.append(Garo)    
else:
    for i in range(N):
        Where, How = list(map(int, input().split()))
        if Where == 0: # 가로로 자르기
            if not SeroL:
                SeroN = Sero - How
                SeroL.append(str(How)) 
                SeroL.append(str(SeroN))
                SeroL.sort()
            else:
                SeroN = int(SeroL[0]) - How
                SeroL.remove(SeroL[0])
                SeroL.append(str(How)) 
                SeroL.append(str(SeroN))
                SeroL.sort()

        if Where == 1: # 세로로 자르기
            if not GaroL:
                GaroN = Garo - How
                GaroL.append(str(How)) 
                GaroL.append(str(GaroN))
                GaroL.sort()
            else:
                GaroN = int(GaroL[0]) - How
                GaroL.remove(GaroL[0])
                GaroL.append(str(How)) 
                GaroL.append(str(GaroN))
                GaroL.sort()

SeroL.sort(reverse=True)
GaroL.sort(reverse=True)

print(int(SeroL[0]) * int(GaroL[0]))'
'''