
def fun(ls,n):
    c=0
    for i in range(n):
        mi=ls.index(min(ls[i:]))
        #print(mi,end=" ")
        if ls[mi]<ls[i]:
            #print("hi",end=" ")
            ls[i],ls[mi]=ls[mi],ls[i]
            c+=1
    return c    
        


n=int(input())
ls=list(map(int,input().split()))
p=fun(ls,n)
print(p)