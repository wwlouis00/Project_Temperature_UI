# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FTP.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#FTP
from ctypes import *
import os
import sys
import ftplib
import time

today = time.strftime('%Y%m%d',time.localtime(time.time()))
ip = '111.111.111.6'
username = 'ftpUserName' 
password = 'ftpPassWord'
filename = '203200189'+ today + 'A001.tar.gz'
src_file = '/ftpFilePath/'+filename
#FTP

#FTP
class myFtp:
    ftp = ftplib.FTP()
    ftp.set_pasv(False) 
    
    def __init__(self,host,port=21):
        self.ftp.connect(host,port)
    
    def Login(self,user,passwd):
        self.ftp.login(user,passwd)
        print(self.ftp.welcome)
 
    def DownLoadFile(self,LocalFile,RemoteFile): #下載指定目錄下的指定檔案
        file_handler = open(LocalFile,'wb')
        print(file_handler)
        # self.ftp.retrbinary("RETR %s" % (RemoteFile),file_handler.write)#接收伺服器上檔案並寫入本地檔案
        self.ftp.retrbinary('RETR ' + RemoteFile,file_handler.write)
        file_handler.close()
        return True

    def DownLoadFileTree(self,LocalDir,RemoteDir): # 下載整個目錄下的檔案
        print("remoteDir:",RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
            self.ftp.cwd(RemoteDir)
            RemoteNames = self.ftp.nlst()
            print("RemoteNames",RemoteNames)
            for file in RemoteNames:
                Local = os.path.join(LocalDir,file)
                print(self.ftp.nlst(file))
            if file.find(".") == -1:
                if not os.path.exists(Local):
                    os.makedirs(Local)
                    self.DownLoadFileTree(Local,file)
                else:
                    self.DownLoadFile(Local,file)
                    self.ftp.cwd("..")
                    return True

    #從本地上傳檔案到ftp
    def uploadfile(self,remotepath,localpath):
        bufsize = 1024
        fp = open(localpath,'rb')
        ftp.storbinary('STOR ' + remotepath,fp,bufsize)
        ftp.set_debuglevel(0)
        fp.close() 

    def close(self):
        self.ftp.quit()
    ####################################################################

class Ui_MainWindow(QtWidgets.QWidget):

    def test(self):   
        
        ip=self.lineEdit.text()
        filedir=self.lineEdit_2.text()
        username=self.lineEdit_3.text()
        password=self.lineEdit_4.text()
        filename=self.lineEdit_5.text()
        #ftp = myFtp('輸入目標檔案IP位置') 
        try:
            ftp = myFtp(ip)
        except ConnectionRefusedError :
            QtWidgets.QMessageBox.warning(self,'錯誤','IP連線失敗',QMessageBox.Ok)
            return
        except TimeoutError:
            QtWidgets.QMessageBox.warning(self,'錯誤','IP連線失敗',QMessageBox.Ok)
            return
        #'192.168.43.185'
        #ftp.Login('username','password')
        try:
            ftp.Login(username,password)
        except ftplib.error_perm:
            QtWidgets.QMessageBox.warning(self,'錯誤','使用者帳密錯誤',QMessageBox.Ok)
            return
        #ftp.DownLoadFile('filename','file path' )
        try:
            ftp.DownLoadFile(filename,filedir)
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self,'錯誤','檔案路徑錯誤',QMessageBox.Ok)
            return
        #ftp.DownLoadFile('test.txt','/home/ncut/Desktop/test.txt' )    
        ftp.close()
        QMessageBox.information(self,'檔案資訊',str(filename)+'下載成功',QMessageBox.Ok)
        print("ok!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 200, 111, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 200, 351, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 320, 71, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 320, 351, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 450, 93, 28))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 280, 101, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 80, 501, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 240, 351, 22))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 280, 351, 22))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 410, 241, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("C:/Users/Howard/Downloads/unnamed (4).jpg"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 360, 71, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 360, 351, 22))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.test)
        self.lineEdit.setText('192.168.43.185')
        self.lineEdit_2.setText('/home/ncut/Desktop/test.txt')
        self.lineEdit_3.setText('ncut')
        self.lineEdit_4.setText('ncut')
        self.lineEdit_5.setText('test.txt')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "連線主機IP位置"))
        self.label_2.setText(_translate("MainWindow", "檔案路徑"))
        self.pushButton.setText(_translate("MainWindow", "送出"))
        self.label_3.setText(_translate("MainWindow", "連線主機帳號"))
        self.label_4.setText(_translate("MainWindow", "連線主機密碼"))
        self.label_5.setText(_translate("MainWindow", "FTP遠端連接傳輸檔案"))
        self.label_7.setText(_translate("MainWindow", "檔案名稱"))

