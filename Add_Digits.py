n=int(input())
while True:
    n=list(str(n))
    p=0
    for i in n:
        p+=int(i)
    if p<10:
        print(p)
        exit()
    n.clear()
    n=str(p)
    
    