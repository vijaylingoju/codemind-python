n,k=map(int,input().split())
ls=list(map(int,input().split()))
c=ls.count(k)
for i in range(n):
    t=ls[i]
    for j in range(i+1,n):
        t+=ls[j]
        if t<=k:
            if t==k:
                c+=1
                break
print(c)  