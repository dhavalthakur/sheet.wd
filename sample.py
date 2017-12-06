
from tkinter import *
from ScrolledText import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter
import os
from tkinter.messagebox import *
from tkinter.filedialog import *
root = Tk(className=" Just another Text Editor")
textPad = ScrolledText(root, width=100, height=80)


# create a menu & define functions for each menu item

def open_command():
    file = tkinter.filedialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()


def save_command(self):
    file = tkinter.filedialog.asksaveasfile(mode='w')
    if file != None:
        data = self.textPad.get('1.0', END + '-1c')
        file.write(data)
        file.close()


def exit_command():
    if tkinter.messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def about_command():
    label = tkinter.messagebox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")


def dummy():
    print("I am a Dummy Command, I will be removed in the next step")


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

#
textPad.pack()
root.mainloop()