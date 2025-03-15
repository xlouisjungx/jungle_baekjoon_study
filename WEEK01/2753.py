# ----- 선언 구간 -----
year = int(input())

# ----- 문제 해결 구간 -----

# 윤년 -> 연도가 4의 배수인것이 필수, 100의 배수가 아닐 때 또는 400의 배수일 때

if year % 4 == 0:
    if(year % 100 != 0 or year % 400 == 0):
        print("1")
    else:
        print("0")

else:
    print("0")