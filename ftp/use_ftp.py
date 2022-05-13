# -*- coding: UTF8 -*-
# 2022-3-8
# 作者：小藍棗
# python連線ftp伺服器
from ftplib import FTP

def conn_ftp():
    '''
     作用：連線ftp伺服器
     引數：無
     返回：ftp伺服器連線的物件
    '''
    
    # FTP連線資訊
    ftp_ip = "192.168.50.34"
    # 預設埠21
    ftp_port = 22
    # 如果未指定，使用預設使用者名稱為Anonymous，密碼為空
    ftp_user = "pi"
    ftp_password = "123"

    ftp = FTP()
    # 連線ftp
    ftp.connect(ftp_ip, ftp_port)
    # ftp登入
    ftp.login(ftp_user, ftp_password)
    # 檢視歡迎資訊
    print(ftp.getwelcome())
    print("ok")
    return ftp
    
ftp = conn_ftp()