t=int(input())
while t:
    f=0
    n=int(input())
    ls=list(map(int,input().split()))
    #(ls)
    for i in range(len(ls)):
        if sum(ls[:i])==sum(ls[i+1:]):
            print("YES")
            f=1
            break
    if f==0:
        print("NO")
    t-=1    