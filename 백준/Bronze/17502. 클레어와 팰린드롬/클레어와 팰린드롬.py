num = int(input())
str = list(input())

for idx in range(1 , (num//2)+1):
    while True:
       
        if str[idx-1] == '?' and str[num-idx] == '?':
            str[idx-1] = str[num-idx] = 'a'
            break
      
        elif str[idx-1] == str[num-idx]:
            break
 
        elif str[idx-1] == '?':
            str[idx - 1] = str[num-idx]
            break
        elif str[num-idx] == '?':
            str[num - idx] = str[idx - 1]
            break

if str[num//2] == '?':
    str[num // 2] = 'a'



print(''.join(str))
