a,b=map(int,input().split())
ls1=list(set(list(map(int,input().split()))))
ls2=list(set(list(map(int,input().split()))))
ls=ls1+ls2
x=0
for i in ls:
    if i in ls1 and i not in ls2 or i in ls2 and i not in ls1:
        x+=1
print(x)        