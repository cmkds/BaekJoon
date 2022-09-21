def yaksoo(n, lst):
    for i in range(1,n//2+1):
        if n%i == 0:
            lst.append(i)
    lst.append(n)           ########자기 자신을 끝에 약수 리스트에 안넣어서 43%인가에서 틀림
    return lst

a, b = map(int,input().split())

lstA =[]
lstB= []

yaksoo(a,lstA)
yaksoo(b,lstB)
# print(lstA)
# print(lstB)

kyoZipHap = list(set(lstA) & set(lstB))

print(max(kyoZipHap))
print(a*b//(max(kyoZipHap)))