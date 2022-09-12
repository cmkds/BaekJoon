N , chkN = map(int,input().split())
lst = list(map(int,input().split()))

tmpSum = sum(lst[:chkN])
#res = -10000000
res = sum(lst[:chkN])

for i in range(1,N-chkN+1):
    tmpSum = tmpSum - lst[i-1] + lst[i+chkN-1]

    if tmpSum > res:
        res = tmpSum

print(res)