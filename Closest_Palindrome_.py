def ispal(n):
    if str(n)==str(n)[::-1]:
        return 1
    else:
        return 0
n=int(input())
for i in range(1,n):
    if(ispal(n-i)==1 and ispal(n+i)==1):
        print(n-i,end=" ")
        print(n+i,end="")
        break
    elif(ispal(n-i)==1):
        print(n-i)
        break
    elif(ispal(n+i)==1):
        print(n-i)
        break