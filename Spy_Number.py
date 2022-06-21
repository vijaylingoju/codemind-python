n=input()
s,p=0,1
for i in n:
    s+=int(i)
    p*=int(i)
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")