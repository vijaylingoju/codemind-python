n=int(input())
ls=list(map(int,input().split()))
s=0
for i in range(n-1):
    if ls[i]<ls[i+1]:
        s+=(ls[i+1]-ls[i])
print(s)        