import pysftp
import paramiko
import sys

paramiko.util.log_to_file("paramiko.log")

sftpURL   =  'ftp.buysellmove.com'
sftpUser  =  'gavilon'
sftpPass  =  'gAv1l0n/cntr/020620'
localPath =  'temp'

ssh = paramiko.SSHClient()
# automatically add keys without requiring human intervention
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )

ssh.connect(sftpURL, username=sftpUser, password=sftpPass)

ftp = ssh.open_sftp()

ftp.chdir('files/invoice_files/out/')


for i in ftp.listdir():
     if i.endswith('.csv'):
          print(i)
          ftp.get(i, i)

ssh.close()


