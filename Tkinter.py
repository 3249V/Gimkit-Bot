from tkinter import *
from Main import *
import time
root = Tk()
error_var = StringVar()
def stuff():
    print(code.get())
    if code.get() == '':
        error_var.set("You didn't enter a code. Try entering a code")
    else:
        bot = GimkitBot()
        bot.join(code.get())
        time.sleep(2)
        bot.start()



root.title("Gimkit Bot")
root.geometry('400x300')
root.iconbitmap(r'Icon.ico')
root.resizable(False, False)
#root.configure(background = 'white')
title = Label(root, text ="Welcome to the Gimkit Bot!")
title.pack(pady= 10)
title.config(font = ("arial", 20))

code = Entry(root)
code.pack(padx = 10, pady = 10)

start = Button(root, text = "Start", command = stuff)
start.pack(pady = 10)

error_text = Label(root, textvariable = error_var)
error_text.pack(pady = 10)
root.mainloop()