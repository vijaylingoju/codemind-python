a,b=map(int,input().split())
ls1=list((list(map(int,input().split()))))
ls2=list((list(map(int,input().split()))))
ls=list((ls1+ls2))
x=[]
for i in ls:
    if i in ls1 and i not in ls2 or i not in ls1 and i  in ls2:
        x.append(i)
print(*x)        