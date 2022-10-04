n = int(input())

lst = list(map(int,input().split()))

cnt = 0
for i in lst:
    if i == 1:
        cnt -= 1
    for j in range(2,i//2+1):
        if not i%j:
            break
    else:
        cnt += 1

print(cnt)