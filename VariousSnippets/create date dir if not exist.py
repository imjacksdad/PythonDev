import os
import datetime
import shutil

# using now() to get current time 
current_time = datetime.datetime.now()

#Get current month and day
mm = (current_time.month) 
    
dd = (current_time.day) 

sourcedir = '//tepfil01/homes/zec0009/'
print(sourcedir);
print(sourcedir + 'test')

targetdir = '//tepfil01/homes/zec0009/' + str(mm) + '-' + str(dd)
print(targetdir);

# Check whether the specified path exists or not
isExist = os.path.exists(targetdir)

if not isExist:
  
  # Create a new directory because it does not exist 
  #os.makedirs(targetdir)
  print("The new directory is created!")
  copy2(sourcedir,dst) 
