N = int(input())
gidoongLst = [list(map(int, input().split())) for _ in range(N)]

#[[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]
gidoongLst.sort(key=lambda a: a[0])     ##기둥리스트 인덱스 순서대로 정렬0  ###
#[[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

#print(gidoongLst)

####가장 높은 기둥 인덱스 구하기
###다 구하고 len 이 1일랑 2이상일때 따로 계산하기.
maxGidoongLst = []
maxGidoong=0
maxGidoongIdx =0
for idx, gidoong in enumerate(gidoongLst):
   if maxGidoong < gidoong[1]:
       maxGidoong = gidoong[1]
############
for idx, gidoong in enumerate(gidoongLst):
    if maxGidoong == gidoong[1]:
        #maxGidoongLst.append([idx,gidoong[1]])
        maxGidoongLst.append([idx, gidoong[1], gidoong[0]])

#########################################
#print(maxGidoongLst)



leftChkLst = []
tmp = 0
for idx, giddong in enumerate(gidoongLst):
    if idx > maxGidoongLst[0][2]:
        break
    if tmp < giddong[1]:
        tmp = giddong[1]
        leftChkLst.append(giddong)


rightChkLst = []
tmp = 0
for i in range(len(gidoongLst)-1, maxGidoongLst[-1][0] -1, -1):
    if tmp < gidoongLst[i][1]:
        tmp = gidoongLst[i][1]
        rightChkLst.append(gidoongLst[i])




cnt = 0
if len(leftChkLst) > 1:
    for i in range(len(leftChkLst)-1):
        cnt += leftChkLst[i][1] * ( leftChkLst[i+1][0]-leftChkLst[i][0])

#print(leftChkLst)

if len(rightChkLst) > 1:
    for i in range(len(rightChkLst)-1):
        cnt += rightChkLst[i][1] * (rightChkLst[i][0]-rightChkLst[i+1][0])

#print(rightChkLst)

#print(maxGidoongLst)
if len(maxGidoongLst)==1:
    cnt += maxGidoong
else:
    cnt += maxGidoong * (maxGidoongLst[-1][2] - maxGidoongLst[0][2]+1)
print(cnt)