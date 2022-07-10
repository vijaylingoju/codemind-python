n=int(input())
#print(n)
while True:
    n=list(str(n))
    p=0
    for i in n:
        p+=int(i)**2
    if p<10:
        if p==1 or p==7:
            print("True")
            exit()
        else:
            print("False")
            exit()
    n.clear()
    n=str(p)
    
    