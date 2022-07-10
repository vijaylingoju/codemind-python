n=int(input())
p,q,s=0,1,0
while s<n:
    s=p+q
    p=q
    q=s
if s==n:
    print("True")
else:
    print("False")