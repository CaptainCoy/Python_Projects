import tkinter
from tkinter import *
import os
import shutil
from datetime import datetime, timedelta
import tkinter.filedialog

class uiWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        # Building the window
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry("{}x{}".format(700,500))
        self.master.title("File Transfer Interface")
        self.master.config(bg="#80a89b")

        # Headline on window
        self.lblHL = Label(self.master, text="File Transfer", font=("impact", 18), bg="#80a89b", fg="#5c0812")
        self.lblHL.grid(row=0, column=4, padx=(5,5), pady=(5,5))

        # Browse button
        self.btnBrowse = Button(self.master, text="Browse", bg="#277d7a", fg="#c7ad71", width=10, command=chooseFile)
        self.btnBrowse.grid(row=1, column=1, padx=(5,5), pady=(5,5))

        # Origin entry
        self.folderA = Entry(self.master, text=folderPathStart, width=50, bg="#c7ad71", fg="#5c0812")
        self.folderA.grid(row=1, column=2, columnspan=5, padx=(5,5), pady=(5,5))

        # Browse button        
        self.btn1Browse = Button(self.master, text="Browse", bg="#277d7a", fg="#c7ad71", width=10, command=sendFile)
        self.btn1Browse.grid(row=3, column=1, padx=(5,5), pady=(5,5))

        # Destination entry
        self.folderB = Entry(self.master, text=folderPathEnd, width=50, bg="#c7ad71", fg="#5c0812")
        self.folderB.grid(row=3, column=2, columnspan=5, padx=(5,5), pady=(5,5))
        
        # Transfer button
        self.btnTransfer = Button(self.master, text="Transfer", bg="#277d7a", fg="#c7ad71", width=10, command=GetFileList)
        self.btnTransfer.grid(row=5, column=3, padx=(5,5), pady=(5,5))

        # Close button
        self.btnClose = Button(self.master, text="Close", bg="#277d7a", fg="#c7ad71", width=10, command=closeWin)
        self.btnClose.grid(row=5, column=5, padx=(5,5), pady=(5,5))

        # Status display
        self.lblDisplay = Label(self.master, text='', font=('impact', 12), bg="#80a89b", fg="#5c0812")
        self.lblDisplay.grid(row=6, column=4, padx=(5,5), pady=(5,5))

         
def chooseFile():
    name = tkinter.filedialog.askdirectory()
    folderPathStart.set(name)

def sendFile():
    name = tkinter.filedialog.askdirectory()
    folderPathEnd.set(name)

def closeWin():
    self.master.destroy()

def GetFileList():
    
    # Folder of origin
    originPath = '/python_projects/File_Transfer_Assignment/daysWork/'

    # File destination folder
    destinationPath = '/python_projects/File_Transfer_Assignment/Home_Office/'

    # The type of files we are looking for
    fileType = '.txt'

    #Acquiring the current time
    cur_time = datetime.now()

    # Returns the list of directory entries given by originPath  
    files = os.listdir(originPath)


    for i in files:
        file_path = os.path.join(originPath, i)
        # Changing modification time to past 24 hours
        past_24hr = cur_time - timedelta(hours=24)
        # Getting modification date of files
        mod_time = os.path.getmtime(file_path)
        # Converting time from seconds to days
        recentlyUpdated = datetime.fromtimestamp(mod_time)
        if past_24hr < recentlyUpdated:
            shutil.move(originPath + '/' + i, destinationPath)
            print(i + 'Files Transfered!')
            #success.set('Files Transfered')
        else:
            print('Nothing to move...')
           
    
if __name__ == "__main__":
    root = Tk()
    folderPathStart=StringVar()
    folderPathEnd=StringVar()
    App = uiWindow(root)
    root.mainloop()
    
