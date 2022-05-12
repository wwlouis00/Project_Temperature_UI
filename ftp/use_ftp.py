from fileinput import filename
from ftplib import FTP
ftp = FTP()
timeout = 30
port = 22

ftp.connect('192.168.50.51',port,timeout)
ftp.login('pi','123') #登入
print (ftp.getwelcome())
ftp.cwd('/home/pi/socket_cam/result')
list = ftp.nlst()

for test in list:
    print(test)

path = "C:\GitLab" + test

f = open(path,'wb')
filename = 'RETR' + test
ftp.retrbinary(filename,f.write)
ftp.delete(test)
ftp.storbinary('STOR '+filename, open(path, 'rb'))
ftp.quit()