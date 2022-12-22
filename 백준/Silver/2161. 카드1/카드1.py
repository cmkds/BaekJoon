n = int(input())

lst = [i for i in range(1,n+1)]

for i in range(len(lst)):
    a = lst.pop(0)
    if not lst:
        print(a, end='')
        break
    b = lst.pop(0)
    lst.append(b)
    print(a, end=' ')