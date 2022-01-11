# import additional support
import shutil
import datetime
import glob
import os


def GetFileList(path, type):
    return glob.glob(path+'*'+type)

originPath = '/python_projects/File_Transfer_Assignment/daysWork/'
destinationPath = '/python_projects/File_Transfer_Assignment/Home_Office/'
fileType = '.txt'

# create a list of .txt filenames in daysWork folder
fileList = GetFileList(originPath, fileType)

for file in fileList:
    # aquire todays date and last modified date
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()

    filePathList = file.split("//")
    filename = filePathList[-1]

    # if modified within the last 24 hours it will be copied into Home_Office folder
    if modifyDate > todaysDate:
        shutil.copy2(file, destinationPath + filename)


