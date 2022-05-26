n=int(input())
ls=list(map(int,input().split()))
k=int(input())
x=[]
if k not in ls:
    x.append(-1)
    x.append(-1)
    print(*x)
    exit()
x.append(ls.index(k))
ls=ls[::-1]
x.append(n-(ls.index(k))-1)
print(*x)