n=int(input())
a,b,c,d=0,1,0,1
print(a,b,end=" ")
while c+2<n:
    d=a+b
    a=b
    b=d
    print(d,end=" ")
    c+=1