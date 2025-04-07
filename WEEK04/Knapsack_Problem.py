import itertools
import time

# 10
weight = [8, 5, 6, 2, 7, 3]
value = [52, 25, 24, 15, 70, 12]

weight_sub = []
value_total = []

start = time.time()
# weight의 subset 만들기
for i in range(1, len(weight) + 1):
    tmp = itertools.combinations(weight, i)
    weight_sub.extend(tmp)

# subset중 무게가 10kg 미만인 subset의 value합 구하기
for j in range(len(weight_sub)):
    if sum(weight_sub[j]) <= 20:
        value_sum = 0
        for k in range(len(weight_sub[j])):
            value_sum += value[weight.index(weight_sub[j][k])]
        value_total.append(value_sum)

# 최대 value 출력
print("Max Value: %d"%max(value_total))
finish = time.time()

print("Run Time: % fs"%(finish-start))

# Time Complexity
# O(2**n)
# 부분집합의 가짓수를 구하는 것 때문에 그런거 같다고 합니다.