import shutil
import os

# set where the source of the files are
source = '/python_projects/File_Transfer_Assignment/folderA/'

# set the destination path to folderB
destination = '/python_projects/File_Transfer_Assignment/folderB/'
files = os.listdir(source)

for i in files:
    # we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
