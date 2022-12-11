s = int(input())

n = 1
sum = 0
while 1:
    sum += n
    n += 1
    if sum > s:
        n -= 2
        break
print(n)