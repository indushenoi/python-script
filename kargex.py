""" program to pass key value argument o function"""
#argument can be made dynamic but its not in this program
def fun(**kargs):
    b=1
    for k,v in kargs.items():
        b=b*v
        print(k,"has value",v)
    b=b/100
    print(type(kargs))
    print("Simple interest is",b)
fun(amount=2000,rate=3,year=5)
