from ftplib import FTP
#from datetime import date
#from datetime import timedelta
import time
import shutil
from email_file_found import send_email


ftps = FTP('ftp.gavilon.com')  # connect to host, default port
ftps.login(user='Q002345',passwd='gRt0RA8pSz!')

interval = 1  # in seconds.  Can be a decimal

print("Checking BSM FTP site for files...")

ftps.pwd()

# Get All Files
files = ftps.nlst()
fn = 0
for file in files:
   time.sleep(interval)
   if 'cwcexport.FIL' in files:
      try:
         print("Found..." + file)
         send_email("eric.carstensen@gavilon.com", "eric.carstensen@gavilon.com")
         fn += 1
         #ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
          ##ftp_get_file(file)
      except:
         print ("Error: File could not be downloaded or found " + file)
   else:
      print('CSCEXPORT.FIL not found.')
ftps.quit()

