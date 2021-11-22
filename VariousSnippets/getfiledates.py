import os
from datetime import datetime
import time
import shutil
import stat

# Getting the current work directory (cwd)
path = os.getcwd()

dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
    if file.endswith(".py"):
        print(file)

        #look at the file date and sort them into dirs

        # Both the variables would contain time 
        # elapsed since EPOCH in float
        ti_c = os.path.getctime(file)

        #convert float to readable date
        # Converting the time in seconds to a timestamp
        cleantime = datetime.fromtimestamp(ti_c).strftime('%Y-%m-%d')

        #print the directory that is being created
        print(cleantime)

        #Create dir if not exists
        isExist = os.path.exists(cleantime)
        if not isExist:
            os.mkdir(cleantime)
            
        #Copy the file to the new dir
        #print(f"Moving {file} to {cleantime}")
        #shutil.move(file, path + '\\' + cleantime + '\\' + file)
            
            
