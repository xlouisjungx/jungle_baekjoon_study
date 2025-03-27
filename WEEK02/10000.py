#x축 위에 원이 N개 있다. 원은 서로 교차하지 않는다. 하지만, 접할 수는 있다.

#원으로 만들어지는 영역이 몇 개인지 구하는 프로그램을 작성하시오.

#영역은 점의 집합으로 모든 두 점은 원을 교차하지 않는 연속되는 곡선으로 연결될 수 있어야 한다.



# ----- 선언 부분 -----
N = int(input())
stack = []
circles = []
cnt = 0

# ----- 문제 해결 부분 -----
for i in range(N):
    x, r = map(int, input().split())    
    circles.append((x-r, x+r))

circles.sort()

for start, end in circles:
    if not stack or stack[-1] < start:
            cnt += 1  # 새로운 영역 발생
            stack = [end]  # 스택 비우기
        
    else:
         stack[-1] = max(stack[-1], end)   

print(cnt)