n = int(input())
lst = set(map(int,input().split()))

m = int(input())
chkLst = list(map(int,input().split()))


for i in chkLst:
    if i in lst:
        print(1)
    else:
        print(0)