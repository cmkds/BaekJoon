from sys import stdin

n = int(input())
lst = []

for _ in range(n):
    a, b= map(int,stdin.readline().split())
    lst.append((a,b))

lst.sort(key=lambda lst: lst[0])
lst.sort(key=lambda lst: lst[1])

for i in lst:
    print(f'{i[0]} {i[1]}')