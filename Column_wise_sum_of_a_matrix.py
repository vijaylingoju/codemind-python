r,c=map(int,input().split())
mat,mx,s,k=[],0,0,[]
for i in range(r):mat.append(list(map(int,input().split())))
for i in range(c):
    s=0
    for j in range(r):
        s+=mat[j][i]
    k.append(s)    
print(*k)    