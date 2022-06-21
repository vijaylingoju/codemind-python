n=list(input())
for i in n:
    if i=='6':
        p=n.index(i)
        n.remove(i)
        n.insert(p,'9')
        break
print(''.join(n))    