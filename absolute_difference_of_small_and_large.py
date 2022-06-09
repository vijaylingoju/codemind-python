s=input().split()
for i in s:
    mx,mi=0,0
    mx=ord(max(i))
    mi=ord(min(i))
    print((mx-mi),end=" ")    