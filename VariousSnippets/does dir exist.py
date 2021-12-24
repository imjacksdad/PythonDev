import os
import datetime


# using now() to get current time 
current_time = datetime.datetime.now()

#Get current month and day
mm = (current_time.month) 
    
dd = (current_time.day) 


path = '//tepfil01/homes/zec0009/' + str(mm) + '-' + str(dd)
print(path);

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if not isExist:
  
  # Create a new directory because it does not exist 
  os.makedirs(path)
  print("The new directory is created!")
