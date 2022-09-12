##키는 숫자 값은 인덱스

def bingGoTamsaek(num):
    a, b = dic.get(num)
    chulSoo[a][b] =0    #해당숫자 자리를 0으로 바꿔 버림
    cnt =0
    #가로탐색
    for i in range(5):
        if chulSoo[a][i] !=0:
            break
    else:
        cnt +=1
    #세로 탐색
    for i in range(5):
        if chulSoo[i][b] !=0:
            break
    else:
        cnt +=1
    #좌표가 같을때 대각선 탐색
    if a==b:
        for i in range(5):
            if chulSoo[i][i] !=0:
                break
        else:
            cnt +=1
    #좌표가 역대각선일때 역대각선 탐색
    if a+b == 4:
        for i in range(5):
            if chulSoo[i][4-i] !=0:
                break
        else:
            cnt +=1
    return cnt


chulSoo = [list(map(int,input().split())) for _ in range(5)]

bingGo = [list(map(int,input().split())) for _ in range(5)]

# print(chulSoo)
# print(bingGo)

dic=dict()
for i in range(5):
    for j in range(5):
        dic[chulSoo[i][j]]=(i,j)
# print(dic)

cnt = 0
bingGoCnt =0
for i in range(5):
    for j in range(5):
        # a,b = dic.get(bingGo[i][j])
        # print(a,b)
        bingGoCnt += bingGoTamsaek(bingGo[i][j])
        cnt +=1
        if bingGoCnt >=3:
            break
    if bingGoCnt >= 3:
        break
print(cnt)