import os
from datetime import datetime
import time
import shutil
import stat

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
            ti_c = os.path.getctime(file)
            
            #convert float to readable date
            cleantime = datetime.fromtimestamp(ti_c).strftime('%Y-%m-%d')

            #print the directory that is being created
            print(cleantime)
            print (file)

            #Create dir if not exists
            path.exists(cleantime)
            os.mkdir(cleantime, mode = 0o666)
                       
            #Copy the file to the new dir
            print(f"Moving {file} to {cleantime}")
            shutil.copyfile(file, cleantime)
            
            #print(os.path.join(r, file))
            #print(file)
            
