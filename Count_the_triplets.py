n=int(input())
for i in range(n):
    l=int(input())
    a=list(map(int,input().split()))
    a.sort()
    c=0
    for i in range(l):
        for j in range(i+1,l-1):
            if a[i]+a[j] in a[j+1:]:
                c+=1
    if c>0:
        print(c)
    else:
        print(-1)
        