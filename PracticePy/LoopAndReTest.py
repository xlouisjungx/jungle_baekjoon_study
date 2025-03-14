# ----- 선언 구간 -----

'''

#for 반복문 기본 구조
for 변수 in range(시작, 끝):
    print(변수)

'''

print("----- 반복문 출력 구간 -----")

i = 1

for i in range(1, 6):
    print(i, end=" ")
print('\n')

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print('\n')