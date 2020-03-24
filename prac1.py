""" program using function to
        1)create file
        2) read file
        3) append to file
        4) read last line
        5) read first line from 2nd character
    """

def createfile():
    with open("abc.txt","w") as f:
        f.write("python is so simple\n its so simple than java\n everything is in lower case\n no braces instead tab\n")
    f.close()
    print("file created")
def readfile():
    with open("abc.txt","r") as f:
        print(f.read())
    f.close()
def append():
    with open("abc.txt","a") as f:
        f.write("python is interpreted")
    f.close()
    with open("abc.txt","r") as f:
        lst=f.readlines()
        i=1
        for j in lst:
                print(i,j)
                i=i+1
    f.close()
def lastline():
    with open("abc.txt","r") as f:
        lst=f.readlines()
        length=len(lst)
        print(lst[length-1])

def firstline():
    with open("abc.txt","r") as f:
        lst=f.readlines()
        s=lst[0]
        print(s[2:])

        
createfile()
print("*********")
readfile()
print("*********")
append()
print("*********")
print("last line is")
lastline()
print("*********")
print("first line is")
firstline()


      
