# ----- 선언 부분 -----
String = list(map(str, input()))
StrWH = []

# ----- 문제 해결 부분 -----

for i in "abcdefghijklmnopqrstuvwxyz":
    if i in String:
        StrWH.append(String.index(i)) #처음 등장하는 위치 추가
    else:
        StrWH.append(-1)

print(*StrWH)
