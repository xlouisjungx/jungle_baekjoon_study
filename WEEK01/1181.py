# ----- 선언 부분 -----
num = int(input())
stringL = []
S = ''

# ----- 문제 해결 부분 -----
for i in range(num):
    string = str(input())
    stringL.append(string)

stringLS = sorted(set(stringL), key=lambda x: (len(x), x))        

for i in range(len(stringLS)):
    print(stringLS[i])

# set(): 중복된 문자열을 제거
# sorted():
# key=lambda x: (len(x), x)
# 첫 번째 기준 → 문자열 길이
# 두 번째 기준 → 사전순 정렬