n=int(input())
ls=list(map(int,input().split()))
k=int(input())
k=k%n
if k==0:
    print(*ls)
else:    
    print(*ls[-k:]+ls[:n-k])