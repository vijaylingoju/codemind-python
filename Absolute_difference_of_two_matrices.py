r=int(input())
mat1,mat2,mat=[],[],[]
for i in range(r):mat1.append(list(map(int,input().split())))
for i in range(r):mat2.append(list(map(int,input().split())))
for i in range(r):
    mat=[]
    for j in range(r):
        mat.append(abs(mat1[i][j]-mat2[i][j]))
    print(*mat)    