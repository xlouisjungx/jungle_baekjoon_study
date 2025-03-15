# ----- 선언 부분 -----
x, y, w, h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

minx = 0
miny = 0
result = 0

# ----- 문제해결 부분 -----
if x > w-x:
    minx = w-x
elif x < w-x:
    minx = x
elif x == w-x:
    minx = x

if y > h-y:
    miny = h-y
elif y < h-y:
    miny = y
elif y == h-y:
    miny = y

if minx > miny:
    result = miny
elif minx < miny:
    result = minx
elif minx == miny:
    result = minx

print(result)