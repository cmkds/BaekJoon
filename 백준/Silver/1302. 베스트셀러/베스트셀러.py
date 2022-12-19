n = int(input())

dic = {}

for _ in range(n):
    book = input()
    try:
        dic[book] = dic[book] + 1
    except:
        dic[book] = 1
a = dict(sorted(dic.items()))
b = sorted(a.items(), key = lambda x : x[1], reverse=True)

# print(dic)
# print(a)
# print(b)
print(b[0][0])