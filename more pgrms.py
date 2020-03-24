"""for i in [1,23,3,4]:
	if i==6:
		print("hi")
		break
else:
    print(i,"not found")
"""
###################
"""fridge={"eggs":10,"milk":"2lit","bread":"1pkt"}
def in_fridge():
    ''' This is a function to see if the fridge has a food.
    fridge has to be a dictionary defined outside of the function.
    the food to be searched for is in the string eggs '''
    try:
        count = fridge["mil"]
    except KeyError:
        count=0
        print("no key found")
    return count
print(in_fridge.__doc__)
a=in_fridge()
print(a)
"""
########################
"""def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    print(type(integers))
    return result
    
print(my_sum(1, 2, 3))
"""
###################
"""def fact(no):
    if not isinstance(no, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if not no >= 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")

    def inner_fact(no):
        if no==1:
            return 1
        else:
            return no*inner_fact(no-1)
    return inner_fact(no)
num=int(input("enter number"))
print(fact(num))
"""
#######################
"""
class Employee:
    increment=1.5
    no_of_emp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'
        Employee.no_of_emp+=1
    def display(self):
        print("*******")
        print(self.first)
        print(self.last)
        print(self.pay)
        print(self.email)
        print("*******")
    def appraisal(self):
        self.pay=int(self.pay*Employee.increment)# or can use self.increment
emp1=Employee("Rhima","Sen",50000)
emp2=Employee("Abhinav","Jha",60000)
print(Employee.__dict__)
print("###############")
#show with emp1.increment=1.7
print(emp1.__dict__)
emp1.appraisal()
emp2.appraisal()
emp1.display()
emp2.display()
print("no of employees are",Employee.no_of_emp)
"""
##############################

"""class Employee:
    increment=1.5
    def __init__(self,first,last,pay,age):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'
        self.age=age
    def display(self):
        print("*******")
        print(self.first)
        print(self.last)
        print(self.pay)
        print(self.email)
        a=int(self.age)
        print(self.age,Employee.isadult(a))
        print("*******")
    def appraisal(self):
        self.pay=int(self.pay*Employee.increment)
    @classmethod
    def changeappraisal(cls,amt):
        cls.increment=amt
    @classmethod
    def createobj(cls,data):
        first,last,pay,age=data.split('-')
        return cls(first,last,pay,age)
    @staticmethod
    def isadult(age):
        if age>=18:
            return "Adult"
        return "Not Adult"
str1="deepa-roy-50000-19"
str2="riya-sen-70000-17"
emp1=Employee.createobj(str1)
emp2=Employee.createobj(str2)
emp1.display()
emp2.display()
print(Employee.increment)
print(emp1.increment)
print(emp2.increment)
Employee.changeappraisal(1.7)
print(Employee.increment)
print(emp1.increment)
print(emp2.increment)
print(help(Employee))
print(dir(Employee))
"""
###############
"""class Employee:
    increment=1.5
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def appraisal(self):
        self.pay=int(self.pay*self.increment)
class Developer(Employee):
    increment=1.7
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
class Manager(Employee):
    increment=1.8
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_tmmem(self):
        print(self.first,"is the Manager of",end=' ')
        for i in self.employees:
            print(i.first,end=' ')
        print()
dev1=Developer('Smith','John',50000,'python')
dev2=Developer('Deepa','Pai',40000,'java')
dev1.appraisal()
dev2.appraisal()
print(dev1.first," ",dev1.pay)
print(dev2.first," ",dev2.pay)
mngr1=Manager('Reshma','Dude',80000)
mngr1.appraisal()
print(mngr1.first," ",mngr1.pay)    
mngr1.add_emp(dev1)
mngr1.add_emp(dev2)
mngr1.print_tmmem()
mngr1.rem_emp(dev2)
mngr1.print_tmmem()
mngr2=Manager('Pinky','Gupta',90000,[dev2])
mngr2.print_tmmem()
"""
###################
"""def add(a,b=None):
    if b is None:
        return a
    return a+b
print(add(2,3))
print(add("indu ","shenoi"))
print(add([1,2],[3,4]))
print(add(2))
"""
###################
class Parent:
    def __init__(self,first,last):
        self.__first=first
        self._last=last
    def display(self):
        print("Parent's name is ",self.__first,self._last)

class Child(Parent):
    def __init__(self,first,par):
        self.first=first
        self.last=par._last
    def display(self):
        print("Child's name is ",self.first,self.last)
p=Parent("Sajit","Sharma")
p.display()
c=Child("Anusree",p)
c.display()
print(p._last)
print(p._Parent__first)
"""
try:
    a=int(input("enter no"))
    b=int(input("enter no"))
    c=a/b
except ZeroDivisionError as arg:
    print(arg)
else:
    print(c)


"""
