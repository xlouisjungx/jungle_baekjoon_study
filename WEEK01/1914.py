# ----- 선업 구간 -----
def Top(num: int, st: int, fn: int):

    ## 바닥 타일 총합 6인거 활용

    if num > 1: ## 처음(앎) -> 중간(모름) // 마지막 값 (알고있음)
         #Top(num-1, st(고정)), fn)
         Top(num-1, st, 6-fn-st)

    print(st, fn)

    if num > 1: ## 중간(모름) --> 마지막(앎)) // 처음(앎)
         #Top(num-1, st, fn{고정)})
         Top(num-1, 6-st-fn, fn)
    

# ----- 문제 해결 구간 -----
num = int(input())

print(2**num - 1)

if num <= 20:
    Top(num,1 ,3)