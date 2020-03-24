"""program to pass n no of argument in fuction at run time not possible in any other language"""

def simple(*kargs):
    p=0
    for v in kargs:
        p=p+v
    
    print(p)

n=int(input("enter no of argument for fn"))
l=[]
for i in range(n):
    v=int(input("enter no"))
    l.append(v)
print(l)
simple(*l)
