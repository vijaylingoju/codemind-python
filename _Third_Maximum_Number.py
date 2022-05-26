n=int(input())
ls=list(map(int,input().split()))
ls=sorted(set(ls))[::-1]
#print(ls)
if len(ls)>2:
    print(ls[2])
else:
    print(max(ls))