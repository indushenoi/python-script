"""program to input age and if age is <0 and >100 catch error"""

def age():
    global a
    a=int(input("enter the age"))
    if(a<0)or (a>100):
        raise ValueError
try:
    a=None
    age()
except ValueError:
     print("age should between 0 and 100")
else:
     print("age is",a)
        
        
        
    
