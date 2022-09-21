from itertools import combinations

#N M K # 1~N 까지 수 M개 고르기 적어도 K개 같기

N, M, K = map(int,input().split())

lst = list(i for i in range(1,N+1))   ### 1~N까지 리스트 한번에 만들기

a = list(combinations(lst,M))
#print(a)  [(1,), (2,), (3,)]

chk = a[0]
# print(len(chk))
# print(chk)

cnt = 0
for aa in a:
    tmpCnt = 0
    for aaa in aa:
        if aaa in chk:
            tmpCnt +=1
    if tmpCnt >=K:
        cnt +=1
print(cnt/len(a))