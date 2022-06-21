n=input()
s=0
k=n
n=str(int(n)**2)
for i in n:
    s+=int(i)
if s==int(k):
    print("Neon Number")
else:
    print("Not Neon Number")