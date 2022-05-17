import ftplib
host = '192.168.50.240'
username = 'pi'
password = '123'

f = ftplib.FTP(host)
f.login(username, password)  


def ftp_download():
    '''以二進位制形式下載檔案'''
    file_remote = 'log.txt'
    file_local = 'D:\\test_data\\ftp_download.txt'
    bufsize = 1024  # 設定緩衝器大小
    fp = open(file_local, 'wb')
    f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
    fp.close()

def ftp_upload():
    '''以二進位制形式上傳檔案'''
    file_remote = 'ftp_upload.txt'
    file_local = 'D:\\test_data\\ftp_upload.txt'
    bufsize = 1024
    fp = open(file_local, 'rb')
    f.storbinary('STOR ' + file_remote, fp, bufsize)
    fp.close()
 
ftp_download()
ftp_upload()
f.quit()