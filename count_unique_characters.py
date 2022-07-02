a='abcdefghijklmnopqrstuvwxyz'
s=list(input().lower())
while ' ' in s:
    s.remove(' ')
x=0
for i in a:
    if (i in s and s.count(i)==1):
        x+=1
print(x)        