from tkinter import *
from tkinter.filedialog import askopenfilename

def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("Why would you need help?")
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)

scanmenu = Menu(menu)
menu.add_cascade(label="Scan", menu=scanmenu)
scanmenu.add_command(label="New", command=NewFile)
scanmenu.add_command(label="Open...", command=OpenFile)
scanmenu.add_separator()
scanmenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()