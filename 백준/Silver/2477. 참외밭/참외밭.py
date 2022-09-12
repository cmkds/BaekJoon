K = int(input())

lst=[[],[],[],[],[]]
chkLst =[[],[],[],[],[]]
chk=0
for a in range(6):

    idx , giri = map(int,input().split())
    if idx ==1:
        lst[1].append(giri)
        chkLst[1].append(chk)
    elif idx == 2:
        lst[2].append(giri)
        chkLst[2].append(chk)
    elif idx == 3:
        lst[3].append(giri)
        chkLst[3].append(chk)
    else:
        lst[4].append(giri)
        chkLst[4].append(chk)
    chk +=1

for i in range(1,5):
    if len(chkLst[i]) ==2:
        if chkLst[i][1]-chkLst[i][0] !=2:
            lst[i].reverse()



if len(lst[2])==2 and len(lst[3])==2:
    print(K*(lst[4][0]*lst[1][0] - lst[2][1]*lst[3][0]))
elif len(lst[2])==2 and len(lst[4])==2:
    print(K*(lst[3][0]*lst[1][0] - lst[2][0]*lst[4][1]))
elif len(lst[3])==2 and len(lst[1])==2:
    print(K*(lst[2][0]*lst[4][0] - lst[3][1]*lst[1][0]))
elif len(lst[4])==2 and len(lst[1])==2:
    print(K*(lst[2][0]*lst[3][0] - lst[1][1]*lst[4][0]))