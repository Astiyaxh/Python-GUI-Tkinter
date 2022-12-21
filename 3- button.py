from tkinter import *

root = Tk()

# Creating Lable Widget
myLable1 = Label(root, text="Hello world!")
myLable2 = Label(root, text="My Name Is Reza Mehri")
myLable3 = Label(root, text="                     ")

# myLable1 = Label(root, text="Hello world!").grid(row=0, column=0)
# myLable2 = Label(root, text="My Name Is Reza Mehri").grid(row=1, column=2)
# myLable3 = Label(root, text="                     ").grid(row=1, column=1)

# Shoving it onto the screen
myLable1.grid(row=0, column=0)
myLable2.grid(row=1, column=2)
myLable3.grid(row=1, column=1)

root.mainloop()