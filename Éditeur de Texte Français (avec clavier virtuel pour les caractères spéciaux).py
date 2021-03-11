#! /usr/bin/python3
#! /usr/bin/env python3

from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.font as font
import pyperclip







window = Tk()
window.title("Francais")
window.geometry('1950x1000')

myFont = font.Font(size=25)









textarea = scrolledtext.ScrolledText(window, undo=True, width = 100,height = 24,)
textarea['font'] = ('Arial', '25')
textarea.place(x=1, y=55)











def a1():
    textarea.insert(INSERT,'à')


a1 = Button(window, text="à", bg='#0052cc', fg='#ffffff', command=a1 )
a1.grid(column=1, row=1)
a1['font'] = myFont





def a2():
    textarea.insert(INSERT,'À')

a2 = Button(window, text="À", bg='#0052cc', fg='#ffffff', command=a2)
a2.grid(column=2, row=1)
a2['font'] = myFont







def a3():
    textarea.insert(INSERT,'â')

a3 = Button(window, text="â", bg='#0052cc', fg='#ffffff', command=a3)
a3.grid(column=3, row=1)
a3['font'] = myFont






def a4():
    textarea.insert(INSERT,'Â')

a4 = Button(window, text="Â", bg='#0052cc', fg='#ffffff', command=a4)
a4.grid(column=4, row=1)
a4['font'] = myFont











def c1():
    textarea.insert(INSERT,'ç')

c1 = Button(window, text="ç", bg='#0052cc', fg='#ffffff', command=c1)
c1.grid(column=5, row=1)
c1['font'] = myFont



def c2():
    textarea.insert(INSERT,'Ç')

c2 = Button(window, text="Ç", bg='#0052cc', fg='#ffffff', command=c2)
c2.grid(column=6, row=1)
c2['font'] = myFont




def e1():
    textarea.insert(INSERT,'é')

e1 = Button(window, text="é", bg='#0052cc', fg='#ffffff', command=e1)
e1.grid(column=7, row=1)
e1['font'] = myFont





def e2():
    textarea.insert(INSERT,'É')

e2 = Button(window, text="É", bg='#0052cc', fg='#ffffff', command=e2)
e2.grid(column=8, row=1)
e2['font'] = myFont





def e3():
    textarea.insert(INSERT,'è')

e3 = Button(window, text="è", bg='#0052cc', fg='#ffffff', command=e3)
e3.grid(column=9, row=1)
e3['font'] = myFont





def e4():
    textarea.insert(INSERT,'È')

e4 = Button(window, text="È", bg='#0052cc', fg='#ffffff', command=e4)
e4.grid(column=10, row=1)
e4['font'] = myFont





def e5():
    textarea.insert(INSERT,'ê')

e5 = Button(window, text="ê", bg='#0052cc', fg='#ffffff', command=e5)
e5.grid(column=11, row=1)
e5['font'] = myFont







def e6():
    textarea.insert(INSERT,'Ê')

e6 = Button(window, text="Ê", bg='#0052cc', fg='#ffffff', command=e6)
e6.grid(column=12, row=1)
e6['font'] = myFont







def i1():
    textarea.insert(INSERT,'î')

i1 = Button(window, text="î", bg='#0052cc', fg='#ffffff', command=i1)
i1.grid(column=13, row=1)
i1['font'] = myFont





def i2():
    textarea.insert(INSERT,'Î')

i2 = Button(window, text="Î", bg='#0052cc', fg='#ffffff', command=i2)
i2.grid(column=14, row=1)
i2['font'] = myFont






def o1():
    textarea.insert(INSERT,'ô')

o1 = Button(window, text="ô", bg='#0052cc', fg='#ffffff', command=o1)
o1.grid(column=15, row=1)
o1['font'] = myFont



def o2():
    textarea.insert(INSERT,'Ô')

o2 = Button(window, text="Ô", bg='#0052cc', fg='#ffffff', command=o2)
o2.grid(column=16, row=1)
o2['font'] = myFont




def o3():
    textarea.insert(INSERT,'œ')

o3 = Button(window, text="œ", bg='#0052cc', fg='#ffffff', command=o3)
o3.grid(column=17, row=1)
o3['font'] = myFont




def o4():
    textarea.insert(INSERT,'Œ')

o4 = Button(window, text="Œ", bg='#0052cc', fg='#ffffff', command=o4)
o4.grid(column=18, row=1)
o4['font'] = myFont





def u1():
    textarea.insert(INSERT,'ù')

u1 = Button(window, text="ù", bg='#0052cc', fg='#ffffff', command=u1)
u1.grid(column=19, row=1)
u1['font'] = myFont






def u2():
    textarea.insert(INSERT,'Ù')

u2 = Button(window, text="Ù", bg='#0052cc', fg='#ffffff', command=u2)
u2.grid(column=20, row=1)
u2['font'] = myFont





def u3():
    textarea.insert(INSERT,'û')

u3 = Button(window, text="û", bg='#0052cc', fg='#ffffff', command=u3)
u3.grid(column=21, row=1)
u3['font'] = myFont







def u4():
    textarea.insert(INSERT,'Û')

u4 = Button(window, text="Û", bg='#0052cc', fg='#ffffff', command=u4)
u4.grid(column=22, row=1)
u4['font'] = myFont





def g1():
    textarea.insert(INSERT,'«')

g1 = Button(window, text="«", bg='#0052cc', fg='#ffffff', command=g1)
g1.grid(column=23, row=1)
g1['font'] = myFont





def g2():
    textarea.insert(INSERT,'»')

g2 = Button(window, text="»", bg='#0052cc', fg='#ffffff', command=g2)
g2.grid(column=24, row=1)
g2['font'] = myFont





def eu():
    textarea.insert(INSERT,'€')

eu = Button(window, text="€", bg='#0052cc', fg='#ffffff', command=eu)
eu.grid(column=25, row=1)
eu['font'] = myFont











def clr():
    textarea.delete('1.0', END)

eu = Button(window, text="Clear Page", bg='#0052cc', fg='#ffffff', command=clr)
eu.grid(column=27, row=1)
eu['font'] = myFont








window.mainloop()




