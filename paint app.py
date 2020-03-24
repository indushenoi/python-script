""" Program to draw and erase using tkinter"""

from tkinter import *
def paint(event):
    x1,y1=(event.x-10),(event.y-10)
    x2,y2=(event.x+10),(event.y+10)
    c.create_oval(x1,y1,x2,y2,fill="black")
def erase(event):
    x1,y1=(event.x-10),(event.y-10)
    x2,y2=(event.x+10),(event.y+10)
    c.create_oval(x1,y1,x2,y2,fill="grey",outline="grey")

root=Tk()
root.title("paint")
c=Canvas(root,height=100,width=100,bg="grey")
c.pack(expand=YES,fill=BOTH)
c.bind("<B1-Motion>",paint)
c.bind("<B3-Motion>",erase)

l=Label(root,text="click and drag mouse(left to draw and right to erase")
l.pack(side=BOTTOM)
root.mainloop()
