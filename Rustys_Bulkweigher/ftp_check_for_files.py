from ftplib import FTP
import fnmatch
import shutil
from email_file_found import send_email

ftps = FTP('10.141.8.239')  # connect to host, default port
ftps.login(user='admin',passwd='admin')
filename = '*.foosdfgsfdbdsfg'

print("Checking Dimmitt FTP site for files...")

ftps.pwd()

ftps.cwd('Data')

# Get All Files
files = ftps.nlst()
fn = 0
for file in files:
   try:
       fn += 1
       if fnmatch.fnmatch(file, filename):
          print("Found..." + file)
          send_email("eric.carstensen@gavilon.com", "eric.carstensen@gavilon.com,")
          #ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
          #ftp_get_file(file)
       else:
          break
   except:
        print ("Error: File could not be downloaded or found " + file)
ftps.quit()

