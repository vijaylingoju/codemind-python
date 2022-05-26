t=int(input())
while t:
    n1,n2=map(int,input().split())
    ls1=list(map(int,input().split()))
    ls2=list(map(int,input().split()))
    ls1=sorted(ls1+ls2)
    print(*ls1)
    t-=1