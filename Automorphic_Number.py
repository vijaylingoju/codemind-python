n=int(input())
p=len(str(n))
if (n**2)%(10**p)==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")