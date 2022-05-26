n=int(input())
ls=list(map(int,input().split()))
k=int(input())
if k not in ls:
    print('-1')
else:
    print(ls.index(k))