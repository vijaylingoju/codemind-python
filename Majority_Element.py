n=int(input())
ls=list(map(int,input().split()))
p=list(set(ls))
for i in p:
    if ls.count(i)>n//2:
        print(i)
        break
        