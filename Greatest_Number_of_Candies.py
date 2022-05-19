a=int(input())
ls1=list(map(int,input().split()))
b=int(input())
m=max(ls1)
p=[]
for i in ls1:
        p.append((b+i)>=m)
print(*p)
    
    