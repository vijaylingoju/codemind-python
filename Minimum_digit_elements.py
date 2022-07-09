n=int(input())
ls=list(map(int,input().split()))
q=len(str(min(ls)))
c=0
for i in ls:
    if i//(10**q)==0:
        c+=1
print(c)        