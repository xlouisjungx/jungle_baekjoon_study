# ----- 선언 부분 -----

from typing import MutableSequence
import sys

input = sys.stdin.readline
output = sys.stdout.write

def QuikSort(num: MutableSequence, left: int, right: int):
    pl = left # 왼쪽 커서
    pr = right # 오른쪽 커서
    P = num[(pr + pl) // 2] # 피벗

    while pl <= pr: # 두 값이 겹칠떄까지
        while num[pl] < P: # 피벗보다 큰 값을 찾을 때 까지
            pl += 1
        while num[pr] > P: # 피벗보다 작은 값을 찾을 떄 까지
            pr -= 1

        if pl <= pr: # 찾은 두 값이 서로 뒤집혀 있다면, 교환해줘야 피벗 기준으로 정렬
            num[pl], num[pr] = num[pr], num[pl] # 두 값을 바꾼다. --> 분할
            pl += 1
            pr -= 1
            # --> pl, pr이 서로 넘어갔으니, 분할 지점
    
    # 정렬할 배열이 아직 남아있다면 실행함
    if left < pr: # pr을 기준으로 왼쪽 부분
        QuikSort(num, left, pr)
    if pl < right: # pl을 기준으로 오른쪽 부분
        QuikSort(num, pl, right)

def SortNum(num: MutableSequence): # 정렬
    QuikSort(num, 0, len(num)-1)

#num = int(input())
#numL = []

# ----- 문제 해결 부분 -----
#for i in range(num):
    #numN = int(input())
    #numL.append(numN)

#SortNum(numL)

#for i in range(num):
    #print(numL[i])


# 시간 초과 문제 해결하기
num = int(input().strip())  # 첫 줄: 수의 개수
numL = [int(input().strip()) for _ in range(num)]  # N개의 줄에서 정수 입력 받기

numL.sort()

output('\n'.join(map(str, numL)) + '\n')

'''

input = sys.stdin.readline --> 파일로부터 빠르게 한 줄을 읽어들이는 함수로, 대량의 입력을 처리할 때 훨씬 빠름
output = sys.stdout.write --> 한 번에 문자열을 출력할 수 있는 방식이며, 마찬가지로 출력이 더 빠름

num = int(input().strip())  # 첫 줄: 수의 개수 # .strip()을 사용하면 개행 문자를 제거할 수 있음.
numL = [int(input().strip()) for _ in range(num)]  # N개의 줄에서 정수 입력 받기

numL.sort()

output('\n'.join(map(str, numL)) + '\n')


'''