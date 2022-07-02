a='abcdefghijklmnopqrstuvwxyz'
s=list(input().lower())
while ' ' in s:
    s.remove(' ')
x=0
for i in s:
    if s.count(i)==1:
        print(i)
        exit()
print('-1')        