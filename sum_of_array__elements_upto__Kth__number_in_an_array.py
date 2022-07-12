n=int(input())
ls=list(map(int,input().split()))
k=int(input())
i,s=0,0
while ls[i]!=k:
    s+=ls[i]
    i+=1
print(s+ls[i])    