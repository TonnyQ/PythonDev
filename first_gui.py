#!/usr/bin/env python3
#-*- encoding:utf-8 -*-

'''
the first gui
'''

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello,World!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self,text='Hello',command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('message','hello,%s' % name)

app = Application()
app.master.title('Hello,world!')
app.mainloop()
