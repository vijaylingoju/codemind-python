n=int(input())
ls=list(map(int,input().split()))
x=[]
for i in range(len(ls)):
    p=1
    for j in range(len(ls)):
        if i!=j:
            p*=ls[j]
    x.append(p)
print(*x)    