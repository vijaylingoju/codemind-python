n=int(input())
c1,c2=0,0
matrix=[]
for i in range(n):
    a=[]
    a=list(map(int,input().split()))
    matrix.append(a)
for i in range(n):
   # print(matrix[i])
   for j in range(n):
        if i==j:
            c1+=matrix[i][j]
        if i+j==n-1:
            c2+=matrix[i][j]
print("Principal Diagonal:%d" %c1)  
print("Secondary Diagonal:%d" %c2)