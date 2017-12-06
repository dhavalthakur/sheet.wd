import urlhandler
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import messagebox
import urllib.request
import urllib.parse
import urllib.error
import urlhandler
import os
import laminus2

class htmlgrab(self):
    browserwindow = Tk()
    label = Label(browserwindow, text='url:')
    entry = Entry(browserwindow)
    button = Button(browserwindow, text='Go', command=go)
    text = Text(browserwindow)

    browserwindow.mainloop()

def go(self):
    self.text.delete(1.0, END)
    conn = urlhandler.urlhandler(entry.get())
    conn.openURL()
    text.insert(INSERT, conn.getURLdata())
    conn.closeURL()


browserwindow.title('browser')
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side=TOP)