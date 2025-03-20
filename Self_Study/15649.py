# ----- 선언 부분 -----
N, M = list(map(int, input().split()))

def FindPermutation(N, M, path):

    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    
    for i in range(1, N+1):
        # 값을 중복되지 않게하도록...순열
        if i not in path:
            FindPermutation(N, M, path + [i])

# ----- 문제 해결 부분 -----
FindPermutation(N, M, [])