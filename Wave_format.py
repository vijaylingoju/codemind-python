n=int(input())
ls=list(map(int,input().split()))
ls=sorted(ls)[::-1]
for i in range(0,n-1,2):
    ls[i],ls[i+1]=ls[i+1],ls[i]
print(*ls)