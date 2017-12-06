from tkinter import *

def donothing():
    print("okey okey i won't...")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project..",command=donothing)
subMenu.add_command(label="New ..",command=donothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=donothing)
editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="redo",command=donothing)
root.mainloop()
