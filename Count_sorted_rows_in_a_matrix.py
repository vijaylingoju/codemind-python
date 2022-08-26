a,b=map(int,input().split())
mat,c=[],0
for i in range(a):
    p=[]
    p=(list(map(int,input().split())))
    mat.append(p)
for i in mat:
    #print(i)
    if i==sorted(i) or i==sorted(i,reverse=True):
        c+=1
print(c)