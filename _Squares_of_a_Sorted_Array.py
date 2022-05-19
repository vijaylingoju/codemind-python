n=int(input())
ls=list(map(int,input().split()))
for i in range(n):
    ls[i]=ls[i]*ls[i];
print(*sorted(ls))