n,k=map(int,input().split())
ls=list(map(int,input().split()))
#print(n,k,ls)
c=0
for i in ls:
    if i%k!=0:
        c+=1
print(c)        