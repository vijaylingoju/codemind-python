n=int(input())
ls=list(map(int,input().split()))
if ls==sorted(ls) and len(set(ls))==len(ls):
    print("yes")
else:
    print("no")