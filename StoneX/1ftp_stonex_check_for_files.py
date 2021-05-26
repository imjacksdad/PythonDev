from ftplib import FTP
#from datetime import date
#from datetime import timedelta
#import time
#import shutil
from email_stonex_file_found import send_email
from ftp_stonex import ftp_get_file


ftps = FTP('ftp.gavilon.com')  # connect to host, default port
ftps.login(user='Q001022',passwd='Fo2wMQO0e')

print("Checking StoneX FTP site for files...")

ftps.pwd()

# Get All Files
files = ftps.nlst()
fn = 0
for file in files:
#    time.sleep(interval)
    try:
        print("Found..." + file)
        fn += 1
        ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
        ftp_get_file(file)  #calls the ftp file and downloads the file.
    except:
        print ("Error: File could not be downloaded or found " + file)

if fn > 0:
    print(str(fn) + " files found")
##    send_email("eric.carstensen@gavilon.com", "imjacksdad@gmail.com,")
##    print("Email sent")
ftps.quit()

