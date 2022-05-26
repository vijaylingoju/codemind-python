n=int(input())
ls=list(map(int,input().split()))
for i in range(len(ls)):
    if ls.count(ls[i])>1:
        print(ls[i])
        break