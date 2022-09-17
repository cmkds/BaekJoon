N = int(input())
lst = []

for _ in range(N):
  start, end = map(int, input().split())
  lst.append([start, end])

lst = sorted(lst, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
lst = sorted(lst, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
cnt = 0  # 회의 개수를 저장할 변수

for i, j in lst:
  if i >= last:  # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    cnt += 1
    last = j


print(cnt)