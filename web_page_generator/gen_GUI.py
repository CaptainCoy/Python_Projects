# Importing tkinter
import tkinter 
from tkinter import *

# Importing the web_page_generator file and assosiated features
import web_page_generator
import webbrowser
import os


# Building the GUI
class GenWin(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry("{}x{}".format(690, 420))
        self.master.title("Web Page Generator")
        self.master.config(bg="maroon")

        self.varText = StringVar()

        self.lblText = Label(self.master, text="Enter Text: ", font=("impact", 15), bg="maroon", fg="skyblue2")
        self.lblText.grid(row=2, column=2, padx=(5,5), pady=(5,5))

        self.txtText = Entry(self.master, text=self.varText, font=("impact", 20), bg="thistle4", fg="skyblue2")
        self.txtText.grid(row=3, column=4, rowspan=5, columnspan=10, padx=(5,5), pady=(5,5))

        self.btnSubmit = Button(self.master, text="Enter", width=30, bg="skyblue4", fg="limegreen", command=webbrowser.open_new_tab(filename))
        self.btnSubmit.grid(row=9, column=3, padx=(5,5), pady=(5,5))
        
        self.btnSubmit = Button(self.master, text="Exit", width=30, bg="skyblue4", fg="red", command=self.exit)
        self.btnSubmit.grid(row=9, column=5, padx=(5,5), pady=(5,5))

# Adding funtionality to the buttons
    def enter(self):
        self.webbrowser.open_new_tab(filename)
        


    def exit(self):
        self.master.destroy()

# Defining filepath
filename = "C:\python_projects\web_page_generator\index.html"


# Action
if __name__ == "__main__":
    root = Tk()
    App = GenWin(root)
    root.mainloop()
