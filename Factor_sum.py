ls=list(map(int,input().split(',')))

def fun(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s        

f=0
x=[]
for i in ls:
     p=fun(i)
     if p in ls:
         f=1
         x.append(i)
x=sorted(x)
if f==0:
    print("-1")
else:    
    print(*x)