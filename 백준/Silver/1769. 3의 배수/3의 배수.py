n = input()

def chk(cnt,n):

    if len(n)==1:
        print(cnt)
        if n=='3' or n =='6' or n =='9':
            print('YES')
        else:
            print('NO')
        return

    nLst = [int(char) for char in n]
    n = str(sum(nLst))
    cnt += 1

    # if len(n)>=1:
    chk(cnt,n)





chk(0, n)