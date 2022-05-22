n=int(input())
ls=list(map(int,input().split()))
c=0
x=[]
for i in range(n):
    if ls[i]==1:
        c+=1
    else:
        x.append(c) 
        c=0
x.append(c)        
print(max(x))                