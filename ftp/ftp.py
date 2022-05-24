from ftplib import FTP
import os
ftp = FTP('192.168.50.237')

ftp.login(user='pi',passwd='123')

dirname = '/home/pi/socket_cam/result/'
ftp.cwd(dirname)
files = ftp.nlst()
for filename in files:
    if os.path.isfile(filename):
        print("Downloading ......")
        ftp.retrbinary("RETR %s " %filename,open(filename,'wb').write)
ftp.close()