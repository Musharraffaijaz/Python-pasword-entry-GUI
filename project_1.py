#creating an entry box in python 

from tkinter import *


def Submit():
   userText = entry.get()
   print("You entered: " + userText)

def Delete():
   deleteText = entry.delete(0, END)
   print("The entered text wad deleted!")

def Backspace():
   backspaceText = entry.delete(len(entry.get()) - 1, END)
   print("You clicked the backspace button!!")

window = Tk()
window.title('Password Entry')

entry = Entry(window, font=('Poppins', 20), show= '*', fg='darkgreen')

entry.pack(side=LEFT)

submit_button = Button(window, text='Submit', command=Submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='Delete', command=Delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text='Backspace', command=Backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()