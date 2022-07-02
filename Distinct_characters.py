a='abcdefghijklmnopqrstuvwxyz'
s=list(input().lower())
while ' ' in s:
    s.remove(' ')
x=[]    
for i in a:
    if (i in s and s.count(i)==1) and i not in x:
        x.append(i)
print(''.join(x))        