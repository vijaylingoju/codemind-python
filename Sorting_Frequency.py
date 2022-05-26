n=int(input())
ls=list(map(int,input().split()))
p=sorted(list(set(ls)))
x,l=[],[]
for i in p:
    x.append(ls.count(i))
for i in range(len(x)):
    z=x.index(max(x))
    l.append(p[z])
    x[z]=0
print(*l)