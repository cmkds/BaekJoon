n= int(input())

aLst = list(map(int,input().split()))
bLst = list(map(int,input().split()))

aLst.sort()
bLst.sort(reverse=True)
# print(aLst)
# print(bLst)

res = 0
for i in range(n):
    res += aLst[i]*bLst[i]

print(res)