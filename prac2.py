""" using function
    1) read specified line from a file
    2) print content of file in reverse order
    """
    
def line():
    no=int(input("enter line no"))
    with open("abc.txt","r") as f:
        data=f.readlines()
        length=len(data)
        if no<=0 or no>length:
            print("No such line")
        else:
            print(data[no-1])

def rev():
    with open("abc.txt","r") as f:
        data=f.readlines()
        for i in reversed(data):
            print(i)
line()
rev()
