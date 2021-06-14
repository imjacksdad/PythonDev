from ftplib import FTP
from datetime import date
from datetime import timedelta
import time
import shutil


#def ftp_get_file(fname):
def ftp_get_file():
    ftps = FTP('ftp.gavilon.com')  # connect to host, default port
    ftps.login(user='Q001022',passwd='Fo2wMQO0e')

    interval = .5  # in seconds.  Can be a decimal

    # Get today's date 
    today = date.today() 
    print("Today is: ", today)

    #format the date to look like 20210819(yyyymmdd)
    stonex_tdate = today.strftime("%Y%m%d")
    print("StoneX's Date Today = ", stonex_tdate)
    
    # Yesterday date 
    yesterday = today - timedelta(days = 1) 
    print("Yesterday was: ", yesterday)

    #format the date to look like 20210819(yyyymmdd)
    stonex_ydate = yesterday.strftime("%Y%m%d")
    print("StoneX's Date Yesterday = ", stonex_ydate)

    #Set the name of the file including the date (today or yesterday)
    fname = "GAVPOS_" + stonex_ydate
    file = fname

    print("File we're looking for is: ", file)

    ftps.pwd()

    #print("listing here:")
    #ftps.retrlines('LIST')
    # Get All Files
    files = ftps.nlst()

    for file in files:
    #    time.sleep(interval)
        if file.startswith(fname):
            try:
                print("Downloading..." + file)
                ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
            except:
                print ("Error: File could not be downloaded " + file)

            #print('Moving ' + file + ' to \\tedfil01\InformaticaDEV\Process\Position\StoneX')
            #shutil.move(file, '\\\\tedfil01\\InformaticaDEV\\Process\\Position\\StoneX\\' + file)
            #ftp.delete(file)
            #ftp.delete('MONEYFILE.csv')
            #print("File Moved")   
        
    ftps.quit()

ftp_get_file()

#if exists, delete the gavpos file
shutil.copy('GAVPOS_20210519_EOD.csv', 'C:\\Python39\\DEVFiles\\PythonDev\\Support Files\\GAVPOS.csv') # complete target filename given
#if exists in new dir, then print("File Copied.")
#else print("Something went wrong")


