t=int(input())
while t:
    n=int(input())
    ls=list(map(int,input().split()))
    print(int(n*(n+1)/2)-sum(ls))
    t-=1