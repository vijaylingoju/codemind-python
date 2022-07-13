n=int(input())
ls=list(map(int,input().split()))
c=0
for i in ls:
    if i <=(sum(ls)//n):
        c+=1
print(c)        
        