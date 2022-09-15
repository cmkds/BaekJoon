n , m= map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
y = [list(map(int,input().split())) for i in range(n)]

newLst =[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        newLst[i][j] = x[i][j] + y[i][j]

for lst in newLst:
    print(*lst)