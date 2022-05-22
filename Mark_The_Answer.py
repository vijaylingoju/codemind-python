n,m=map(int,input().split())
ls=list(map(int,input().split()))
c,end=0,0
for i in ls:
    if end==2:
        break
    if i<=m:
        c+=1
    else:
        end+=1
print(c)        