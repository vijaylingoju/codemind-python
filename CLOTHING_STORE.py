n=int(input())
ls=list(map(int,input().split()))
p=set(ls)
c=0
for i in p:
    c+=ls.count(i)//2   
print(c)    
        