import os
from datetime import datetime
import time
import shutil
import stat
import win32con, win32api

# Getting the current work directory (cwd)
path = os.getcwd()

#path = 'P:/'

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith(".py"):
            #look at the file date and sort them into dirs

            # Both the variables would contain time 
            # elapsed since EPOCH in float
            ti_c = os.path.getctime(path)
            
            #convert float to readable date
            cleantime = datetime.fromtimestamp(ti_c).strftime('%Y-%m-%d')

            #print the directory that is being created
            print(cleantime)

            #Create dir if not exists
            os.makedirs(cleantime, exist_ok=True)

            #make dir read/write
            os.chmod(cleantime, stat.S_IWRITE )
                       
            #Copy the file to the new dir
            print(f"Moving {file} to {cleantime}")
            shutil.copyfile(file, cleantime)
            
            #print(os.path.join(r, file))
            #print(file)

            #print(f"{file} was created at {cleantime}")
                  #and was last modified at {ti_m}")

