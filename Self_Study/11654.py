# ----- 선언 부분 -----
N = input()

# ----- 문제 해결 부분 -----
if N == int:
    print(chr(N)) # 아스키 코드를 문자로 변환
else:
    print(ord(N)) # 문자를 아스키 코드로 변환
