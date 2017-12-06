from tkinter import *
from tkinter import Menu
import ScrolledText
import tkinter.messagebox
import tkinter.filedialog



root=Tk(className="Project Laminus")


def dummy():
    print ("I am a Dummy Command,I will be removed in the next step")

def open_file():
    f = tkinter.askopenfile(defaultextension=".txt", filetypes=[("All Types", ".*")])
    if not f:
        return
    txt1.delete(1.0, END)
    txt1.insert(END, f.read())
    f.close()

def file_save():
    fout = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    text2save = str(self.text.get(0.0, END))
    fout.write(text2save)
    fout.close()

textPad = ScrolledText.ScrolledText(root,width=200,height=80)



def exit():
    if tkinter.messagebox.askokcancel("Exiting Laminus!", "Do you really want to quit? Save your work if you haven't!"):
        root.destroy()

def about():
    label=tkinter.messagebox.showinfo("About Laminus","Laminus is made by Dhaval Thakur for the aid of programming")


menu = Menu(root)
menubar = Menu(root)
root.configure(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_command(label='Open a File..', command=open_file)
filemenu.add_cascade(label="About..",command=about)
filemenu.add_command(label='Exit Laminus', command=exit)
#*****LOGO****
photo = PhotoImage(file="laminus.gif")
label= Label(root,image=photo)
label.pack()
textPad.pack()

root.mainloop()