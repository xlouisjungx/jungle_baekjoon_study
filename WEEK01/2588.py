# ----- 변수 선업 구간 -----
A = int(input())
B = int(input())

three = 0
four = 0
five = 0
six = 0

# ----- 문제 해결 구간 -----
three = (A * ((B % 100) % 10))
four = (A * ((B % 100) // 10))
five = (A * (B // 100))
six = (five * 100) + (four * 10) + three

print(three)
print(four)
print(five)
print(six)