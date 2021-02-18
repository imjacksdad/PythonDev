from ftplib import FTP
#from datetime import date
#from datetime import timedelta
#import time
import shutil


ftps = FTP('ftp.buysellmove.com')  # connect to host, default port
ftps.login(user='gavilon',passwd='gAv1l0n%%2Fcntr%%2F020620')

interval = .5  # in seconds.  Can be a decimal

print("Checking BSM FTP site for files...")

ftps.pwd()

# Get All Files
files = ftps.nlst()
fn = 0
##for file in files:
###    time.sleep(interval)
##    try:
##        #print("Found..." + file)
##        fn += 1
##        #ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
##        ##ftp_get_file(file)
##    except:
##        print ("Error: File could not be downloaded or found " + file)
ftps.quit()

