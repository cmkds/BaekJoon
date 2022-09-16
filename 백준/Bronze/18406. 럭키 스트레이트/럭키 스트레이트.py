a = list(input())

left = 0
right = 0
for i in range(len(a)//2):
    left += int(a[i])
for i in range(len(a)//2,len(a)):
    right += int(a[i])

if left == right:
    print('LUCKY')
else:
    print('READY')