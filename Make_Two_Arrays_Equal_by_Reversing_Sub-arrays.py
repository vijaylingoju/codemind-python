n1=int(input())
ls1=list(map(int,input().split()))
n2=int(input())
ls2=list(map(int,input().split()))
if sorted(ls1)==sorted(ls2):
    print("True")
else:
    print("False")