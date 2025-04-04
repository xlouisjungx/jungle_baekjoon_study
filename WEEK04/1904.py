def find_ZeroOne(N):
    a = 1
    b = 2
    c = 0

    for i in range(2, N+1):
        c = a
        a = b
        b = (c + b) % 15746
        
        
    return a 

N = int(input())
print(find_ZeroOne(N))

'''
처음 코드(메모리 초과 일어나서 다시 시도)
|
v

def find_ZeroOne(N):
    F = [0] * (N + 1)

    F[0] = 1 # 1번
    F[1] = 2
    F[2] = 3

    for i in range(3, N+1):
        F[i] = F[i-1] + F[i-2]

    return F[N-1] % 15746 

N = int(input())
print(find_ZeroOne(N))
'''