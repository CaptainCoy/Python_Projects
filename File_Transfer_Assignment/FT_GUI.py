import os
import shutil
import datetime
import glob
import tkinter as tk
from tkinter import *


def GetFileList(path, type):
    return glob.glob(path+'*'+type)

originPath = '/python_projects/File_Transfer_Assignment/daysWork/'
destinationPath = '/python_projects/File_Transfer_Assignment/Home_Office/'
fileType = '.txt'


#Make Window
win = tk.Tk()
win.geometry("420x420")
win.title("File Transfer Interface")
win.resizable(0,0)
win.configure(background='#80a89b')

#Create elements
frame = tk.Frame(win, bd=1, relief='sunken', width=150, height=300)
lbl = tk.Label(text="Browse Files: ", bg="#80a89b", fg="#7a5f05")
scrollbar = tk.Scrollbar(frame)
lbox = tk.Listbox(frame)

btn = tk.Button(win, bg='#6a7a6d', fg='#e8c500', width=15)
btn.config(text='Run')

btn1 = tk.Button(win, bg='#6a7a6d', fg='#e8c500', width=15)
btn1.config(text='Exit')

#create a list of .txt filenames in daysWork folder
flist =os.listdir('/python_projects/File_Transfer_Assignment/daysWork')

#Attach listbox to scrollbar
lbox.config(bg='#c7ad71', yscrollcommand=scrollbar.set)
scrollbar.config(command=lbox.yview)

#Poulate listbox
for item in flist:
    lbox.insert(tk.END, item)

#Pack elements
lbl.pack()
frame.pack(side='top')
scrollbar.pack(side='right', fill='y')
lbox.pack()
btn.pack(padx=(10,10), pady=(10,10))
btn1.pack(padx=(10,10), pady=(10,10))


def exit(win):
        win.destroy()

for file in fileList:
    # aquire todays date and last modified date
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()

    filePathList = file.split("//")
    filename = filePathList[-1]

    # if modified within the last 24 hours it will be copied into Home_Office folder
    if modifyDate > todaysDate:
        shutil.copy2(file, destinationPath + filename)

win.mainloop()
