n=int(input())
s,p=1,1
while s<n:
    s=p*(p+1)
    p+=1
    #print(s)
if s==n:
    print("YES")
else:
    print("NO")