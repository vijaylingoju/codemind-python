a,b=map(int,input().split())
ls1=list(set(list(map(int,input().split()))))
ls2=list(set(list(map(int,input().split()))))
ls=list(set(ls1+ls2))
x=0
for i in ls:
    if i in ls1 and i in ls2:
        x+=1
print(x)        