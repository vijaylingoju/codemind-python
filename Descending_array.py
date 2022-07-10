n=int(input())
ls=list(map(int,input().split()))
if ls==sorted(ls)[::-1]:
    print("yes")
else:
    print("no")