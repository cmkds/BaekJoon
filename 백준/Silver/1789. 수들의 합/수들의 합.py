s = int(input())

a = 1
while 1:
    s -= a
    if s <= a:
        break
    a +=1
print(a)