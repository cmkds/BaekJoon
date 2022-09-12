lst = []
for _ in range(9):
    lst.append(int(input()))


res2 = [[]]

for i in lst:
    size = len(res2)

    for j in range(size):
        res2.append(res2[j]+[i])

for lst in res2:
    if len(lst) ==7 and sum(lst)==100:
        a = sorted(lst)

for b in a:
    print(b)