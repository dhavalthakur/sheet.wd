import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import messagebox
import urllib.request
import urllib.parse
import urllib.error
import urlhandler
import sys
import os
from tkinter import PhotoImage, messagebox, Toplevel, Tk, Text
import shlex


class Laminus:
    root = Tk()
    bootstrapdefaultfile =open('bootstrapdefault.txt')
    
    bootstrapdefault=''
    for line in bootstrapdefaultfile:
        bootstrapdefault=bootstrapdefault+'\n'+line
    bootstrapdefaultfile.close()
    materialdefaultfile=open('materialdefault.txt')
    materializedefault = ''
    for line2 in materialdefaultfile:
        materializedefault = materializedefault + line2
    materialdefaultfile.close()

    bootandmaterialfile = open('bootandmaterial.txt')
    bootandmaterialdefault = ''
    for line3 in bootandmaterialfile:
        bootandmaterialdefault = bootandmaterialdefault + '\n' + line3
    bootandmaterialfile.close()

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    editmenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)
    runmenu= Menu(menubar,tearoff=0)
    documentmenu=Menu(menubar,tearoff=0)
    scrollbr = Scrollbar(textarea)
    tfile = None
    photo =PhotoImage(file="laminus.gif")
    label = Label(root,image=photo)
    intro = PhotoImage(file="logo.gif")










    def __init__(self, **window):


        try:
            self.wwwidth = window['width']
        except KeyError:
            pass

        try:
            self.wheight = window['height']
        except KeyError:
            pass







        # set the window text
        self.root.title("new code sheet - sheet.wd Beta 2")



        # center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()


        left = (screenWidth / 2) - (self.wwwidth / 2)
        top = (screenHeight / 2) - (self.wheight / 2)
        bgtext = "black"
        bgcolor = "darkgrey"
        self.root.geometry('%dx%d+%d+%d' % (self.wwwidth, self.wheight, left, top))
        textarea = Text(root, bg=bgcolor, fg=bgtext)
       

        # add controls (widget)
        self.textarea.grid(sticky=N + E + S + W)
        self.textarea.bind("<Control-n>", self.new)
        self.textarea.bind("<Control-o>", self.opentext)
        self.textarea.bind("<Control-s>", self.savetext)
        self.textarea.bind("<Control-Shift-s>", self.savehtml)
        self.textarea.bind("<Control-N>", self.new)
        self.textarea.bind("<Control-O>", self.opentext)
        self.textarea.bind("<Control-S>", self.savetext)
        self.textarea.bind("<Control-Shift-S>", self.savehtml)

        label4 = Label(text="Sheet.wd: Lightweight Text Editor. version 0.1")
        label4.grid(row=1)

        self.filemenu.add_command(label="Samosa Wizard",command=self.introstart)
        self.filemenu.add_command(label="Start a New Sheet", command=self.new, accelerator="Ctrl+N")
        self.filemenu.add_command(label="Start a Bootstrap site",command=self.newbootstrap)
        self.filemenu.add_command(label="Start a materialize site",command=self.startmaterial)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Edit a Text File", command=self.opentext , accelerator="Ctrl+O")
        self.filemenu.add_command(label="Edit a Webpage", command=self.openhtml)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save as txt", command=self.savetext)
        self.filemenu.add_command(label="Save as html", command=self.savehtml)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit this Sheet", command=self.__quitApplication,accelerator="Alt+F4")
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu.add_command(label="Cut", command=self.cuttext)
        self.editmenu.add_command(label="Copy", command=self.copytext)
        self.editmenu.add_command(label="Paste", command=self.pastetext)
        self.editmenu.add_command(label="Go To...", underline=0, command=self.edit_goto, accelerator="Ctrl+G")
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)


        self.documentmenu.add_command(label="Bootstrap",command=self.bootstrap)
        self.menubar.add_cascade(label="Libraries",menu=self.documentmenu)
        self.menubar.add_cascade(label="Run", menu=self.runmenu)
        self.runmenu.add_command(label="Run in browser", command=self.aboutsoft)

        self.helpmenu.add_command(label="About Sheet.wd", command=self.aboutsoft)
        self.helpmenu.add_command(label="grab html code", command=self.htmlgrab)
        self.menubar.add_cascade(label="Misc", menu=self.helpmenu)

        self.root.config(menu=self.menubar)
        self.scrollbr.pack(side=RIGHT, fill=Y)
        self.scrollbr.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scrollbr.set)

    def backchangeblack(self):
        bgcolor="black"
        bgtext="white"
        self.textarea = Text(self.root, bg=bgcolor, fg=bgtext)

    def backchangegreen(self):
        self.bgcolor="black"
        self.bgtext="green"

    def htmlgrab(self):
        exec(open("./htmlgrabber.py").read())

    def newbootstrap(self):
        result = self.save_if_modified()
        if result != None:  # None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.textarea.delete(1.0, "end")
            self.textarea.insert(END,self.bootstrapdefault)
            self.textarea.edit_modified(False)
            self.textarea.edit_reset()
            self.file_path = None
            self.root.title("Bootstrap file")


    def newbootandmaterial(self):
        result = self.save_if_modified()
        if result != None:  # None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.textarea.delete(1.0, "end")
            self.textarea.insert(END,self.bootandmaterialdefault)
            self.textarea.edit_modified(False)
            self.textarea.edit_reset()
            self.file_path = None
            self.root.title("Boot+Material file")

    def startmaterial(self):
        result = self.save_if_modified()
        if result != None:  # None => Aborted or Save cancelled, False => Discarded, True = Saved or Not modified
            self.textarea.delete(1.0, "end")
            self.textarea.insert(END, self.materializedefault)
            self.textarea.edit_modified(False)
            self.textarea.edit_reset()
            self.file_path = None
            self.root.title("Materialize css file")

    def openURL(self):
        self.data = urllib.urlopen(self.address)

    def getURLdata(self):
        return self.data.read()

    def closeURL(self):
        self.data.close()

    def __quitApplication(self):
        self.root.destroy()

        # exit()


    def savetext(self):

        if self.file_path == None:
            result = self.file_save_as()
            self.root.title(os.path.basename(self.tfile) + " - sheet.wd")
        else:
            result = self.file_save_as(filepath=self.file_path)
            self.root.title(os.path.basename(self.tfile) + " - sheet.wd")
        return result

    def file_save_as(self, event=None, filepath=None):
        if filepath == None:
            filepath = filedialog.asksaveasfilename(filetypes=(
                ('Text files', '*.txt'), ('Python files', '*.py *.pyw'),
                ('All files', '*.*')))  # defaultextension='.txt'
            try:
                with open(filepath, 'wb') as f:
                    text = self.textarea.get(1.0, "end-1c")
                    f.write(bytes(text, 'UTF-8'))
                    self.textarea.edit_modified(False)
                    self.file_path = filepath
                    return "saved"
            except FileNotFoundError:
                print('FileNotFoundError')
                return "cancelled"



        else:
            file = open(self.tfile, "w")
            file.write(self.textarea.get(1.0, END))
            file.close()


    def introstart(self):
        root3 = Toplevel()
        iwwidth = 600
        iwheight = 1024
        screenWidthiw = root3.winfo_screenwidth()
        screenHeightiw = root3.winfo_screenheight()

        left = (screenWidthiw / 2) - (iwwidth / 2)
        top = (screenHeightiw / 2) - (iwheight / 2)
        root3.geometry('%dx%d+%d+%d' % (iwwidth, iwheight, left, top))

        root3.title("sheet.wd Starting Wizard")
        #photo3 = PhotoImage(file="logomini.gif" ,width=40)
        #label3 = Label(root3, image=photo3,width=40)
        #label3.grid(column=1)
        button1 =Button(root3,command=self.newbootstrap,text="Create Bootstrap File",width=40)
        button1.grid()
        button2=Button(root3,command=self.newbootandmaterial,text="Bootstrap+ Material",width=40)
        button2.grid()
        button3=Button(root3,command=self.__quitApplication,text="Quit Sheet.wd",width=40)
        button3.grid()
        label1=Label(root3,text="Window Settings")
        label1.grid()
        button4 =Button(root3,command=self.backchangeblack,text="Back and white Contrast")
        button4.grid()
        button5 = Button(root3, command=self.backchangegreen, text="Back and green Contrast")
        button5.grid()

        root3.mainloop()


    def save_if_modified(self, event=None):
        if self.textarea.edit_modified():
            response = messagebox.askyesnocancel("Save?",
                                                 "This document has been modified. Do you want to save changes?")  # yes = True, no = False, cancel = None
            if response:  # yes/save
                result = self.savetext()
                if result == "saved":  # saved
                    return True
                else:  # save cancelled
                    return None
            else:
                return response  # None = cancel/abort, False = no/discard
        else:  # not modified
            return True


    def savehtml(self):

        if self.tfile == None:
            # save as new file
            self.tfile = asksaveasfilename(initialfile='index.html', defaultextension=".html",
                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.html")])

            if self.tfile == "":
                self.tfile = None
            else:
                # try to save the file
                file = open(self.tfile, "w")
                file.write(self.textarea.get(1.0, END))
                file.close()
                # change the window title
                self.root.title(os.path.basename(self.tfile) + " - Sheet.wd")


        else:
            file = open(self.tfile, "w")
            file.write(self.textarea.get(1.0, END))
            file.close()

    def opentext(self):

        self.tfile = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), (" Documents", "*.txt")])

        if self.tfile == "":
            self.tfile = None
        else:
            # try to open the file
            # set the window title
            self.root.title(os.path.basename(self.tfile) + " - sheet.wd Text File Opening")
            self.textarea.delete(1.0, END)

            file = open(self.tfile, "r")

            self.textarea.insert(1.0, file.read())

            file.close()

    def openhtml(self):

        self.tfile = askopenfilename(defaultextension=".html",
                                      filetypes=[("All Files", "*.*"), (" Documents", "*.html")])

        if self.tfile == "":
            self.tfile = None
        else:
            self.root.title(os.path.basename(self.tfile) + " - sheet.wd :-A WebPage code is being displayed")
            self.textarea.delete(1.0, END)

            file = open(self.tfile, "r")

            self.textarea.insert(1.0, file.read())

            file.close()

    def new(self):
        result = self.save_if_modified()
        if result != None:
            self.textarea.delete(1.0, "end")
            self.textarea.edit_modified(False)
            self.textarea.edit_reset()
            self.file_path = None
            self.root.title("new Code Sheet - sheet.wd")


    def aboutsoft(self):
        root1=Toplevel()
        wwwwidth=1200
        wwheight=400
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        left = (screenWidth / 2) - (wwwwidth / 2)
        top = (screenHeight / 2) - (wwheight / 2)

        root1.geometry('%dx%d+%d+%d' % (wwwwidth, wwheight, left, top))

        root1.grid_rowconfigure(0, weight=1)
        root1.grid_columnconfigure(0, weight=1)
        root1.title("About Sheet.wd")
        photo3 = PhotoImage(file="logo.gif")
        label3 = Label(root1, image=photo3)
        label4=Label(root1,text="Code name sheet.wd is a simple text editor for web developers")
        label5=Label(root1,text="and simple users developed by Dhaval. Current version :- 0.1")
        label6=Label(root1,text="sheet.wd is purely made for web development purpose supporting")
        label7=Label(root1,text="simple txt files and HTML webpages.Although you can edit CSS")
        label8=Label(root1,text="files also,its proper functioning would be given later")
        label9=Label(root1,text="For Suggestions or queries - idhavalthakur@gmail.com")
        label3.pack()
        label4.pack()
        label5.pack()
        label6.pack()
        label7.pack()
        label8.pack()
        label9.pack()
        root1.mainloop()

    def edit_goto(self,event=None):
        from tkinter.simpledialog import askinteger
        line = askinteger('Goto', 'Enter line number:')
        self.textarea.update()
        self.textarea.focus()
        if line is not None:
            maxindex = self.textarea.index(END + '-1c')
            maxline = int(maxindex.split('.')[0])
            if line > 0 and line <= maxline:
                self.textarea.mark_set(INSERT, '%d.0' % line)  # goto line
                self.textarea.tag_remove(SEL, '1.0', END)  # delete selects
                self.textarea.tag_add(SEL, INSERT, 'insert + 1l')  # select line
                self.textarea.text.see(INSERT)  # scroll to line
            else:
                from tkinter.messagebox import showerror
                showerror('sheet Error:Line not Present', 'Oops! That line doesnt exist yet! write more lines :)')



    def cuttext(self):
        self.textarea.event_generate("<<Cut>>")

    def pastetext(self):
        self.textarea.event_generate("<<Paste>>")

    def copytext(self):
        self.textarea.event_generate("<<Copy>>")

    def run(self):
        self.root.mainloop()


    def bootstrap(self):
        root2 = Toplevel()
        width = 1024
        wwheight = 1024
        screenWidth = root2.winfo_screenwidth()
        screenHeight = root2.winfo_screenheight()

        left = (screenWidth / 2) - (width / 2)
        top = (screenHeight / 2) - (wwheight / 2)

        root2.geometry('%dx%d+%d+%d' % (width, wwheight, left, top))

        root2.grid_rowconfigure(0, weight=1)
        root2.grid_columnconfigure(0, weight=1)
        root2.title("Bootstrap infochart")
        photobt = PhotoImage(file="bootstrap.gif")
        labelbt = Label(root2,image=photobt)
        labelbt.grid(row=0,column=0)
        labelheading=Label(root2,text="Glyphs summary")
        labelheading.grid(row=1,column=0)
        glyphs1 = PhotoImage(file="glyphs1.gif")
        glyphs2 = PhotoImage(file="glyphs2.gif")
        glyphs3 = PhotoImage(file="glyphs4.gif")
        glyphs4= PhotoImage(file="glyphs5.gif")
        glyphs5= PhotoImage(file="glyphs6.gif")
        labelbt1 = Label(root2, image=glyphs1)
        labelbt2 = Label(root2, image=glyphs2)
        labelbt3 = Label(root2, image=glyphs3)
        labelbt4 = Label(root2, image=glyphs4)
        labelbt5 = Label(root2, image=glyphs5)
        labelbt1.grid(row=1)
        labelbt2.grid(row=2)
        labelbt3.grid(row=3)
        labelbt4.grid(row=4)
        labelbt5.grid(row=5)

        root2.mainloop()


laminus = Laminus(width=1200, height=800)
laminus.run()
