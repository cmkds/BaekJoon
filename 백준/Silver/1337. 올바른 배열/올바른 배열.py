n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

cnt = 0

for i in lst:  #리스트를 돌리고

    for a in range(-4,1):  ##좌측 4개 우측4개까지확인
        tmpCnt = 0
        for b in range(1,6):  ## 우측 5칸이동
            if i+a+b in lst:
                tmpCnt +=1
        if tmpCnt > cnt:
            cnt = tmpCnt
print(5-cnt)