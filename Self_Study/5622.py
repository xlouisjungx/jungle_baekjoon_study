# 1 2 3 4 5 6 7 8 9 각 다이얼 
# 2 3 4 5 6 7 8 9 10 각 다이얼 소요 시간

# ----- 선언 부분 -----
String = input()

num1 = [' ']
num2 = ['A','B','C'] 
num3 = ['D','E','F']
num4 = ['G','H','I']
num5 = ['J','K','L']
num6 = ['M','N','O']
num7 = ['P','Q','R', 'S']
num8 = ['T','U','V']
num9 = ['W','X','Y','Z']

cnt = 0

# ----- 문제 해결 부분 -----
for i in range(len(String)):
    if String[i] in num1:
        cnt += 2
    elif String[i] in num2:
        cnt += 3
    elif String[i] in num3:
        cnt += 4
    elif String[i] in num4:
        cnt += 5
    elif String[i] in num5:
        cnt += 6
    elif String[i] in num6:
        cnt += 7
    elif String[i] in num7:
        cnt += 8
    elif String[i] in num8:
        cnt += 9
    elif String[i] in num9:
        cnt += 10

print(cnt)        