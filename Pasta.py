a,b=map(int,input().split())
ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
for i in ls2:
    if i not in ls1:
        print("No")
        exit()
    p=ls1.index(i)    
    ls1.remove(ls1[p])
print("Yes")    
        