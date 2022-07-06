s1=input().lower().split()
s2=input().lower().split()
s=s2+s1
x=[]
for i in s:
    if s.count(i)==2 and i not in x:
        x.append(i)
print(*x)        