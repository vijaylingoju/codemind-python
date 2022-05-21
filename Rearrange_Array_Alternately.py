t=int(input())
while t:
    f=0
    n=int(input())
    k=(n+1)//2
    ls=list(map(int,input().split()))
    ls=sorted(ls)[::-1]
    p=[]
    i,j=0,n-1
    while i<j:
        p.append(ls[i])
        p.append(ls[j])
        i+=1
        j-=1
    for i in ls:
        if(i not in p):
            p.append(i)
    print(*p)
    t-=1