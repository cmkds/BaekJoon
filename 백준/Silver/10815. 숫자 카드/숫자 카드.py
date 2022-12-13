import sys
input = sys.stdin.readline
n = int(input())
sang = list(map(int, input().split()))
m = int(input())
deck = list(map(int, input().split()))

sang.sort()


def binary_search(lst, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return 'a'
        elif lst[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(sang, deck[i], 0, n-1):
        print(1, end=' ')
    else:
        print(0, end=' ')