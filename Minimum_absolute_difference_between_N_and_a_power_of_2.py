n=int(input())
d,i=1,1
while d<n:
    d=2**i
    if d<n:
        k=d
    i+=1
if abs(n-d)<abs(n-k):
    print(abs(n-d))
else:
    print(abs(n-k))
    