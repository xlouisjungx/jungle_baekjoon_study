# ----- 선언 구간 -----
Test = "푹 자고 싶다." # 문자열 생성
Test2 = "아무 생각 없이."
Test3 = "1234567"

print("----- 문자열 출력 구간 -----")

print("Test: ", Test)
print("Test2: ", Test2)

print("When ypu access to 1 : ", Test[1]) # 해당 위치에 있는 문자 출력

print("When ypu connect the Test and Test 2 and @ : ", Test + " " + Test2 + " " + "계속")
# 문자열 이어붙이기는 진짜 붙이기만 해주기 때문에, 중간에 공백이 필요하면 따로 넣어줘야 한다.

print("When you print the Test thre times",(Test + " ") * 3) 
# 그냥 선언 해놓은 문자열이 해당 횟수만큼 출력된다고 보면 된다.

print("When ypu slicing Test3 1~4 : ", Test3[1:4]) # 1번부터 3번까지의 문자열을 출력한다.

print("The size of Test : ", len(Test)) # 문자열 길이를 출력한다