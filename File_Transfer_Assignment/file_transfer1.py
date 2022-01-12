# import additional support
import shutil
from datetime import datetime, timedelta
import os


def GetFileList():
    
    # Folder of origin
    originPath = '/python_projects/File_Transfer_Assignment/daysWork/'

    # File destination folder
    destinationPath = '/python_projects/File_Transfer_Assignment/Home_Office/'

    # The type of files we are looking for
    fileType = '.txt'

    # Acquiring the current time
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
        else:
            print('Nothing to move...')

# Execute function
GetFileList()   
