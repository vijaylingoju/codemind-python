s=list(input().lower())
p='abcdefghijklmnopqrstuvwxyz'
ns=0
while ' ' in s:
    s.remove(' ')
for i in s:
    if s.count(i)==1:
        print(i)
        exit()
print('-1')        