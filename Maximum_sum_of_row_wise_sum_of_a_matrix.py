r,c=map(int,input().split())
mat,mx=[],0
for i in range(r):mat.append(list(map(int,input().split())))
for i in mat:
    mx=max(mx,sum(i))
print(mx)    