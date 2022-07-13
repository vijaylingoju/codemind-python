n=int(input())
ls=list(map(int,input().split()))
e,o=[],[]
for i in ls:
    if i%2:
        o.append(i)
    else:
        e.append(i)
o.extend(e)
print(*o)
        