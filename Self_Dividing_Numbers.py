def fun(n):
    t,c,p=n,0,0
    while t:
        d=t%10
        if d==0:
            return 0
        if n%d==0:
            c+=1
        p+=1    
        t=t//10
    if p==c:
        return 1
    else:
        return 0

a=int(input())
b=int(input())
for i in range(a,b+1):
    if fun(i)==1:
        print(i,end=" ")