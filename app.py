# -*- coding: cp1251 -*-
from Tkinter import *
import datetime
import time
import re
from Book import *

root = Tk()
root.title("Book")
root.geometry('440x300') 
frame = Frame(root)
frame.pack()
book=Book()
buttonAdd=Button(frame, text="New Contact", width=30,
                     command=book.addContact)
buttonAdd.grid(row=0, column=0)
buttonAll = Button(frame, text="See all Contacts", width=30,
                     command=book.seeAll)
buttonAll.grid(row=0, column=1)
book.reminder()

root.mainloop()
