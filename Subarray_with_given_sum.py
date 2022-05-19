t=int(input())
while t:
    f=0
    n,k=map(int,input().split())
    ls=list(map(int,input().split()))
    for i in range(n):
        t=ls[i]
        f=0
        for j in range(i+1,n):
            t+=ls[j]
            if t==k:
                f=1
                print(i+1,end=" ")
                print(j+1,end="
")
                break
        if f==1:
            break
        if i==n-1 and f==0:
            print('-1')
        
    t-=1            
  