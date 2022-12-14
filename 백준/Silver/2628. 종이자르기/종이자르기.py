x, y = map(int, input().split())

xLst = [0, x]
yLst = [0, y]

for _ in range(int(input())):
    a, n = map(int, input().split())
    if a:
        xLst.append(n)
    else:
        yLst.append(n)
xLst.sort()
yLst.sort()

# print(xLst)
# print(yLst)
sx = 0
sy = 0
for i in range(len(xLst)):
    sx = max(sx, xLst[i]-xLst[i-1])
for i in range(len(yLst)):
    sy = max(sy, yLst[i]-yLst[i-1])
print(sx*sy)