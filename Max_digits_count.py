n=int(input())
ls=list(map(int,input().split()))
q=len(str(max(ls)))
c,x=0,[]
for i in ls:
    x.append(len(str(i)))
for i in x:
    if i==q:
        c+=1
print(c)        