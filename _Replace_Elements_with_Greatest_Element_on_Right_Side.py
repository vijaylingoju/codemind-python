n=int(input())
ls=list(map(int,input().split()))
x=[]
for i in range(n-1):
    x.append(max(ls[i+1:]))
x.append(-1)
print(*x)
