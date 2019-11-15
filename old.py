from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os
# import tkMessageBox

filename = None

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename 
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    filename = "'"+str(filename)+"'"
    print(filename)

def delete():
    days = txt.get()
    if days.isdigit():
        print(filename)
        print(days)
        os.system("find " + filename + " -atime " + days + " -delete;")
        messagebox.showinfo( "Notice", "Files Deleted Successfully")
    else:
        messagebox.showinfo( "Notice", "Wrong Input")

root = Tk()
root.title("Directory Cleanup")
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)
button3 = Button(text="Delete", command=delete)
button3.grid(row=7, column=3)
lbl2 = Label(master=root,text="Enter the no. of days before which files have to be deleted")
lbl2.grid(row=6, column=1)
txt = Entry(root,width=30)
txt.grid(column=1, row=7)
mainloop()
