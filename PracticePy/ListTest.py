# 기본 구조 : 리스트명 = []

# print("----- 선언 구간 -----")

test = [1, 2, 3, 4, 5]  # 배열 생성

print("----- 리스트 출력 구간 -----")

#print(test[0])  # 첫 번째 요소 접근: 1 --> 리스트나 배열은 첫번째 요소가 0번부터 시작
print("Test List : ", test) # 리스트 출력

test.append(6)  # 요소 추가
print("Test List Append: ", test) # 리스트 출력

test.append([2,4])
print("Test List Append : ", test) # 리스트 출력

test.insert(7, 10) # 해당 위치에 요소 추가
print("Test List Insert : ", test) # 리스트 출력

test.pop()  # 마지막 요소 제거
print("Test List Pop : ", test) # 리스트 출력

test.remove(1) # 특정 값을 제거
print("Test List Remove: ", test) # 리스트 출력

print("Size of List : ", len(test)) # 리스트 길이 값 반환

print("Test List : ", test[5][0]) # 리스트 출력