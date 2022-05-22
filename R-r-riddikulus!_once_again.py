n,k=map(int,input().split())
ls=list(map(int,input().split()))
k=abs(k-n)
k=k%n
if k==0:
    print(*ls)
else:    
    print(*ls[-k:]+ls[:n-k])