from ftplib import FTP
import fnmatch
import shutil


ftps = FTP('10.141.8.239')  # connect to host, default port
ftps.login(user='admin',passwd='admin')
filename = 'Data.zip'

print("Checking BSM FTP site for files...")

ftps.pwd()

# Get All Files
files = ftps.nlst()
fn = 0
for file in files:
   try:
       #print("Found..." + file)
       fn += 1
       if fnmatch.fnmatch(file, filename):
          print("Found..." + file)
          #ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
          #ftp_get_file(file)
   except:
        print ("Error: File could not be downloaded or found " + file)
ftps.quit()

