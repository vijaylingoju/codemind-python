n=int(input())
ls=list(map(int,input().split()))
p=sorted(set(ls))
mx=0

for i in p:
    if ls.count(i)>mx:
        mx=ls.count(i)
        l=i
    if ls.count(i)==mx:
        if i<l:
            l=i
print(l)            