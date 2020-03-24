""" copy content of one file to another"""
with open("e:\\indu\\first.txt","r") as f:
    s=f.read()
with open("e:\\indu\\second.txt","w") as f:
    f.write(s)
print("file copied")
