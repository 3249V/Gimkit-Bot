from tkinter import Tk, StringVar, Label, Button, Entry
import tkinter
from Main import GimkitBot
import time
root = Tk()
error_var = StringVar()

def startcmd():
    if code.get() == '':
        return error_var.set("You didn't enter a code. Try entering a code.")
    GimkitBot(code.get(), nameentry.get())


class EntryWithPlaceholder(tkinter.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

root.title("Gimkit Bot")
root.geometry('400x300')
root.iconbitmap(r'Icon.ico')
root.resizable(False, False)
title = Label(root, text = "Welcome to the Gimkit Bot!")
title.pack(pady = 10)
title.config(font = ("arial", 20))

code = EntryWithPlaceholder(root, placeholder="Game Code")
code.pack(padx = 10, pady = 10)
nameentry = EntryWithPlaceholder(root, placeholder="Username")
nameentry.pack(padx = 10, pady = 10)

start = Button(root, text = "Start", command = startcmd)
start.pack(pady = 10)

error_text = Label(root, textvariable = error_var)
error_text.pack(pady = 10)
root.mainloop()