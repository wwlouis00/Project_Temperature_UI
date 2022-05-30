import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from scipy.interpolate import make_interp_spline
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog,QMessageBox
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
from datetime import datetime, timedelta
from pyzbar import pyzbar
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5 import QtCore, QtGui, QtWidgets
import ftplib
from ctypes import *
from sqlalchemy import false
from sqlalchemy import false
#時間格式
now_output_time = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
com_now_output = str(datetime.now().strftime('%Y-%m-%d'))

def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.timer_camera = QtCore.QTimer()
        self.CAM_NUM = 0
        self.count = 0

        self.timer = QTimer()
        self.qrcode_result1 = []
        self.qrcode_result2 = []
        self.qrcode_result3 = []
        self.qrcode_result4 = []
        self.qrcode_result5 = []
        self.qrcode_result6 = []
        self.qrcode_result7 = []
        self.qrcode_result8 = []

    def display1(self):
        img = cv2.imread("image/CH1.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH1", img)

    def display2(self):
        img = cv2.imread("image/CH2.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH2", img)

    def display3(self):
        img = cv2.imread("image/CH3.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH3", img)

    def display4(self):
        img = cv2.imread("image/CH4.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH4", img)

    def display5(self):
        img = cv2.imread("image/CH5.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH5", img)

    def display6(self):
        img = cv2.imread("image/CH6.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH6", img)

    def display7(self):
        img = cv2.imread("image/CH7.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH7", img)

    def display8(self):
        img = cv2.imread("image/CH8.jpg")
        img = cv2.resize(img, (500, 500))
        cv2.imshow("CH8", img)

    def qrcode1(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode1', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch1_qrcodelable.setText(text)
                self.qrcode_result1.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result1.append("None")
        cv2.destroyAllWindows()

    def qrcode2(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode2', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch2_qrcodelable.setText(text)
                self.qrcode_result2.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result2.append("None")
        cv2.destroyAllWindows()

    def qrcode3(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode3', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch3_qrcodelable.setText(text)
                self.qrcode_result3.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result3.append("None")
        cv2.destroyAllWindows()

    def qrcode4(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode4', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch4_qrcodelable.setText(text)
                self.qrcode_result4.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result4.append("None")
        cv2.destroyAllWindows()

    def qrcode5(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode5', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch5_qrcodelable.setText(text)
                self.qrcode_result5.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result5.append("None")
        cv2.destroyAllWindows()

    def qrcode6(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode6', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch6_qrcodelable.setText(text)
                self.qrcode_result6.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result6.append("None")
        cv2.destroyAllWindows()

    def qrcode7(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode7', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch7_qrcodelable.setText(text)
                self.qrcode_result7.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result7.append("None")
        cv2.destroyAllWindows()

    def qrcode8(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode8', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.ch8_qrcodelable.setText(text)
                self.qrcode_result8.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result8.append("None")
        cv2.destroyAllWindows()
    
    def browsefile(self):
        #宣告計算變數
        self.CH1_data = []
        self.CH2_data = []
        self.CH3_data = []
        self.CH4_data = []
        self.CH5_data = []
        self.CH6_data = []
        self.CH7_data = []
        self.CH8_data = []
        self.CH_T_On = []
        self.CH_T_Off = []
        self.CH_total = []
        self.slot_high = []
        self.slot_low = []
        self.CH_slot = []
        self.TF_array = []
        #開啟TXT檔案
        self.fname = QFileDialog.getOpenFileName(self, '開啟txt檔案', 'C:\Program Files (x86)', 'txt files (*.txt)') # " C:\python\Learn_Python\Temperature" 是自己的電腦位置路徑
        if(self.fname[0]==""):
            print("no file")
        else:
            if not os.path.isdir('./image'):
                print("Directory 'image' does not exist.")
                os.mkdir('./image')
            if not os.path.isdir('./result'):
                print("Directory 'result' does not exist.")
                os.mkdir('./result')
            if not os.path.isdir('./EGGI_Temperature'):
                print("Directory 'EGGI_Temperature' does not exist.")
                os.mkdir('./EGGI_Temperature')
            self.input_file.setText(self.fname[0])
            self.df = pd.read_csv(self.fname[0], delimiter='\t')
            self.df.columns = ['time','index', 'index', 'CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8']  # 在開啟檔案上面新增一行
            print("Open file(.txt) >> " + str(self.fname[0]))
            print("-" * 100)
            print(self.df)
            print("-" * 100)
            # X軸
            for i in range(0, len(self.df.index), 1):
                self.CH_total.append(i)
            # Y軸
            for i in range(0, len(self.df.index), 1):
                self.CH1_data.append(self.df.loc[i, 'CH1'])
                self.CH2_data.append(self.df.loc[i, 'CH2'])
                self.CH3_data.append(self.df.loc[i, 'CH3'])
                self.CH4_data.append(self.df.loc[i, 'CH4'])
                self.CH5_data.append(self.df.loc[i, 'CH5'])
                self.CH6_data.append(self.df.loc[i, 'CH6'])
                self.CH7_data.append(self.df.loc[i, 'CH7'])
                self.CH8_data.append(self.df.loc[i, 'CH8'])
            
            for ch in range(1, 9, 1):
                if ch == 1:
                    self.CH_data = [[self.df.loc[i, 'CH' + str(ch)] for i in range(len(self.df.index))]]
                else:
                    self.CH_data.append([self.df.loc[i, 'CH' + str(ch)] for i in range(len(self.df.index))])
            # 存取每個Channel的值到陣列

            for i in range(0, 8, 1):
                self.T_On_array = []
                self.T_Off_array = []
                # 對一個Channel進行資料搜尋
                for ch in range(0, len(self.df.index) - 1, 1):
                    a = self.CH_data[i][ch + 1] - self.CH_data[i][ch]
                    b = self.CH_data[i][ch] - self.CH_data[i][ch-1]
                    # 達成T_On條件把資料存進self.T_On_array陣列
                    if a < 0 and self.CH_data[i][ch] > 109 and b > 0:
                        self.T_On_array.append(self.CH_data[i][ch])
                        self.slot_high.append(ch)
                    # 達成T_Off條件把資料存進self.T_Off_array陣列
                    if a > 0 and 73 < self.CH_data[i][ch] < 74 and b < 0:
                        self.T_Off_array.append(self.CH_data[i][ch])
                        self.slot_low.append(ch)
                # 溫度資料發生其他狀況
                if self.CH_data[i][0] == -204.8 or self.CH_data[i][2] == self.CH_data[i][3]:
                    # 如果溫度未加熱保持恆溫
                    if self.CH_data[i][2] != -204.8:
                        for j in range(1, 9, 1):
                            self.T_On_array.append(self.CH_data[i][2]) #"恆溫"
                            self.T_Off_array.append(self.CH_data[i][2])
                    # 如果沒有連接上
                    for k in range(1, 9, 1):
                        self.T_On_array.append(0)
                        self.T_Off_array.append(0)
                print(self.T_On_array)
                self.CH_T_On.append(self.T_On_array[0])
                print(self.CH_T_On)
                self.CH_T_Off.append(self.T_Off_array[0])
                value_gap = self.T_On_array[0] - self.T_Off_array[0]
                time_gap = self.slot_high[0] - self.slot_low[0]
                self.CH_slot.append(round(float(value_gap/time_gap),2))
            print("-"*20 + "CH_T_On" + "-"*20) 
            for i in range(0,8,1):
                print(self.CH_T_On[i])
            print("-"*20 + "CH_T_Off" + "-"*20)
            for i in range(0,8,1):
                print(self.CH_T_Off[i])

            # 將On跟Off陣列存取的資料對應至各個位置上
            self.ch1_T_On.setText(str(self.CH_T_On[0]))
            self.ch1_T_Off.setText(str(self.CH_T_Off[0]))
            self.ch2_T_On.setText(str(self.CH_T_On[1]))
            self.ch2_T_Off.setText(str(self.CH_T_Off[1]))
            self.ch3_T_On.setText(str(self.CH_T_On[2]))
            self.ch3_T_Off.setText(str(self.CH_T_Off[2]))
            self.ch4_T_On.setText(str(self.CH_T_On[3]))
            self.ch4_T_Off.setText(str(self.CH_T_Off[3]))
            self.ch5_T_On.setText(str(self.CH_T_On[4]))
            self.ch5_T_Off.setText(str(self.CH_T_Off[4]))
            self.ch6_T_On.setText(str(self.CH_T_On[5]))
            self.ch6_T_Off.setText(str(self.CH_T_Off[5]))
            self.ch7_T_On.setText(str(self.CH_T_On[6]))
            self.ch7_T_Off.setText(str(self.CH_T_Off[6]))
            self.ch8_T_On.setText(str(self.CH_T_On[7]))
            self.ch8_T_Off.setText(str(self.CH_T_Off[7]))
            #####每個Channel的斜率
            self.ch1_slope.setText(str(self.CH_slot[0]))
            self.ch2_slope.setText(str(self.CH_slot[1]))
            self.ch3_slope.setText(str(self.CH_slot[2]))
            self.ch4_slope.setText(str(self.CH_slot[3]))
            self.ch5_slope.setText(str(self.CH_slot[4]))
            self.ch6_slope.setText(str(self.CH_slot[5]))
            self.ch7_slope.setText(str(self.CH_slot[6]))
            self.ch8_slope.setText(str(self.CH_slot[7]))
            #####每個channel結果Pass或Fail
            # 資料對應
            P = "Pass"
            F = "Fail"
            N = "未連接"
            W = "未加熱"
            # 對應顏色
            T_color = "color: green;"
            F_color = "color: gray;"
            constant_color = "color: orange;"
            # 儲存結果

            # CH1PF
            if self.CH_slot[0] == 0 or self.CH_T_On[0] == self.CH_T_Off[0]:
                if self.CH_T_On[0] == self.CH_T_Off[0] != 0:
                    self.ch1_PF.setText(str(W))
                    self.ch1_PF.setStyleSheet(constant_color)
                    self.TF_array.append(str(W))
                else:
                    self.ch1_PF.setText(str(N))
                    self.ch1_PF.setStyleSheet(F_color)
                    self.TF_array.append(str(N))
            else:
                self.ch1_PF.setText(str(P))
                self.ch1_PF.setStyleSheet(T_color)
                self.TF_array.append(str(P))
            # CH2PF
            if self.CH_slot[1] == 0 or self.CH_T_On[1] == self.CH_T_Off[1]:
                if self.CH_T_On[1] == self.CH_T_Off[1] != 0:
                    self.ch2_PF.setText(W)
                    self.ch2_PF.setStyleSheet(constant_color)
                    self.TF_array.append(W)
                else:
                    self.ch2_PF.setText(N)
                    self.ch2_PF.setStyleSheet(F_color)
                    self.TF_array.append(N)
            else:
                self.ch2_PF.setText(P)
                self.ch2_PF.setStyleSheet(T_color)
                self.TF_array.append(P)
            # CH3PF
            if self.CH_slot[2] == 0 or self.CH_T_On[2] == self.CH_T_Off[2]:
                if self.CH_T_On[2] == self.CH_T_Off[2] != 0:
                    self.ch3_PF.setText(W)
                    self.ch3_PF.setStyleSheet(constant_color)
                    self.TF_array.append(W)
                else:
                    self.ch3_PF.setText(N)
                    self.ch3_PF.setStyleSheet(F_color)
                    self.TF_array.append(N)
            else:
                self.ch3_PF.setText(P)
                self.ch3_PF.setStyleSheet(T_color)
                self.TF_array.append(P)
            # CH4PF
            if self.CH_slot[3] == 0 or self.CH_T_On[3] == self.CH_T_Off[3]:
                if self.CH_T_On[3] == self.CH_T_Off[3] != 0:
                    self.ch4_PF.setText(W)
                    self.ch4_PF.setStyleSheet(constant_color)
                    self.TF_array.append(W)
                else:
                    self.ch4_PF.setText(N)
                    self.ch4_PF.setStyleSheet(F_color)
                    self.TF_array.append(N)
            else:
                self.ch4_PF.setText(P)
                self.ch4_PF.setStyleSheet(T_color)
                self.TF_array.append(P)
            # CH5PF
            if self.CH_slot[4] == 0 or self.CH_T_On[4] == self.CH_T_Off[4]:
                if self.CH_T_On[4] == self.CH_T_Off[4] != 0:
                    self.ch5_PF.setText(W)
                    self.ch5_PF.setStyleSheet(constant_color)
                    self.TF_array.append(W)
                else:
                    self.ch5_PF.setText(N)
                    self.ch5_PF.setStyleSheet(F_color)
                    self.TF_array.append(N)
            else:
                self.ch5_PF.setText(P)
                self.ch5_PF.setStyleSheet(T_color)
                self.TF_array.append(P)
            # CH6PF
            if self.CH_slot[5] == 0 or self.CH_T_On[5] == self.CH_T_Off[5]:
                if self.CH_T_On[5] == self.CH_T_Off[5] != 0:
                    self.ch6_PF.setText(W)
                    self.ch6_PF.setStyleSheet(constant_color)
                    self.TF_array.append(W)
                else:
                    self.ch6_PF.setText(N)
                    self.ch6_PF.setStyleSheet(F_color)
                    self.TF_array.append(N)
            else:
                self.ch6_PF.setText(P)
                self.ch6_PF.setStyleSheet(T_color)
                self.TF_array.append(P)
            # CH7PF
            if self.CH_slot[6] == 0 or self.CH_T_On[6] == self.CH_T_Off[6]:
                if self.CH_T_On[6] == self.CH_T_Off[6] != 0:
                    self.ch7_PF.setText(W)
                    self.ch7_PF.setStyleSheet(constant_color)
                    self.TF_array.append(W)
                else:
                    self.ch7_PF.setText(N)
                    self.ch7_PF.setStyleSheet(F_color)
                    self.TF_array.append(N)
            else:
                self.ch7_PF.setText(P)
                self.ch7_PF.setStyleSheet(T_color)
                self.TF_array.append(P)
            # CH8PF
            if self.CH_slot[7] == 0 or self.CH_T_On[7] == self.CH_T_Off[7]:
                if self.CH_T_On[7] == self.CH_T_Off[7] != 0:
                    self.ch8_PF.setText(W)
                    self.ch8_PF.setStyleSheet(constant_color)
                    self.TF_array.append(W)
                else:
                    self.ch8_PF.setText(N)
                    self.ch8_PF.setStyleSheet(F_color)
                    self.TF_array.append(N)
            else:
                self.ch8_PF.setText(P)
                self.ch8_PF.setStyleSheet(T_color)
                self.TF_array.append(P)
            self.take_picture()

            # -----------------------------------------------------------------------
            img = cv2.imread("image/CH1.jpg")
            img2 = cv2.imread("image/CH2.jpg")
            img3 = cv2.imread("image/CH3.jpg")
            img4 = cv2.imread("image/CH4.jpg")
            img5 = cv2.imread("image/CH5.jpg")
            img6 = cv2.imread("image/CH6.jpg")
            img7 = cv2.imread("image/CH7.jpg")
            img8 = cv2.imread("image/CH8.jpg")
            # 轉換影象通道
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
            img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
            img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
            img6 = cv2.cvtColor(img6, cv2.COLOR_BGR2RGB)
            img7 = cv2.cvtColor(img7, cv2.COLOR_BGR2RGB)
            img8 = cv2.cvtColor(img8, cv2.COLOR_BGR2RGB)
            # 獲取影象大小
            x = img.shape[1]
            y = img.shape[0]
            x2 = img2.shape[1]
            y2 = img2.shape[0]
            x3 = img3.shape[1]
            y3 = img3.shape[0]
            x4 = img4.shape[1]
            y4 = img4.shape[0]
            x5 = img5.shape[1]
            y5 = img5.shape[0]
            x6 = img6.shape[1]
            y6 = img6.shape[0]
            x7 = img7.shape[1]
            y7 = img7.shape[0]
            x8 = img8.shape[1]
            y8 = img8.shape[0]
            # 圖片放縮尺度
            # self.zoomscale = 1
            frame = QImage(img, x, y, x * 3, QImage.Format_RGB888)
            self.pix = QPixmap.fromImage(frame)
            frame2 = QImage(img2, x2, y2, x2 * 3, QImage.Format_RGB888)
            self.pix2 = QPixmap.fromImage(frame2)
            frame3 = QImage(img3, x3, y3, x3 * 3, QImage.Format_RGB888)
            self.pix3 = QPixmap.fromImage(frame3)
            frame4 = QImage(img4, x4, y4, x4 * 3, QImage.Format_RGB888)
            self.pix4 = QPixmap.fromImage(frame4)
            frame5 = QImage(img5, x5, y5, x5 * 3, QImage.Format_RGB888)
            self.pix5 = QPixmap.fromImage(frame5)
            frame6 = QImage(img6, x6, y6, x6 * 3, QImage.Format_RGB888)
            self.pix6 = QPixmap.fromImage(frame6)
            frame7 = QImage(img7, x7, y7, x7 * 3, QImage.Format_RGB888)
            self.pix7 = QPixmap.fromImage(frame7)
            frame8 = QImage(img8, x8, y8, x8 * 3, QImage.Format_RGB888)
            self.pix8 = QPixmap.fromImage(frame8)
            # 建立畫素圖元
            self.item = QGraphicsPixmapItem(self.pix)
            self.item2 = QGraphicsPixmapItem(self.pix2)
            self.item3 = QGraphicsPixmapItem(self.pix3)
            self.item4 = QGraphicsPixmapItem(self.pix4)
            self.item5 = QGraphicsPixmapItem(self.pix5)
            self.item6 = QGraphicsPixmapItem(self.pix6)
            self.item7 = QGraphicsPixmapItem(self.pix7)
            self.item8 = QGraphicsPixmapItem(self.pix8)
            # 建立場景
            self.scene = QGraphicsScene()
            self.scene2 = QGraphicsScene()
            self.scene3 = QGraphicsScene()
            self.scene4 = QGraphicsScene()
            self.scene5 = QGraphicsScene()
            self.scene6 = QGraphicsScene()
            self.scene7 = QGraphicsScene()
            self.scene8 = QGraphicsScene()
            self.scene.addItem(self.item)
            self.scene2.addItem(self.item2)
            self.scene3.addItem(self.item3)
            self.scene4.addItem(self.item4)
            self.scene5.addItem(self.item5)
            self.scene6.addItem(self.item6)
            self.scene7.addItem(self.item7)
            self.scene8.addItem(self.item8)
            # 將場景新增至檢視
            self.ch1_chart.setScene(self.scene)
            self.ch2_chart.setScene(self.scene2)
            self.ch3_chart.setScene(self.scene3)
            self.ch4_chart.setScene(self.scene4)
            self.ch5_chart.setScene(self.scene5)
            self.ch6_chart.setScene(self.scene6)
            self.ch7_chart.setScene(self.scene7)
            self.ch8_chart.setScene(self.scene8)
    
    def take_picture(self):
        # ---------------CH1---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH1_data, 'o-', color='red', label="CH1_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH1.jpg')
        # ---------------CH2---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH2_data, 'o-', color='orange', label="CH2_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH2.jpg')
        # ---------------CH3---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH3_data, 'o-', color='yellow', label="CH3_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH3.jpg')
        # ---------------CH4---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH4_data, 'o-', color='green', label="CH4_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH4.jpg')
        # ---------------CH5---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH5_data, 'o-', color='#6F00FF', label="CH5_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH5.jpg')
        # ---------------CH6---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH6_data, 'o-', color='m', label="CH6_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH6.jpg')
        # ---------------CH7---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH7_data, 'o-', color='purple', label="CH7_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH7.jpg')
        # ---------------CH8---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH8_data, 'o-', color='k', label="CH8_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH8.jpg')
    
    def save_log(self):
        if self.input_name.text() == "":
            QtWidgets.QMessageBox.critical(self, u"存取失敗", u"請輸入操作人員", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
            print("請輸入操作人員")
        elif self.input_file.text() == "":
            QtWidgets.QMessageBox.warning(self, u"存取失敗", u"未開啟檔案", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
            print("未開啟檔案")
        elif self.ch1_qrcodelable.text() == "" or self.ch2_qrcodelable.text() == "" or self.ch3_qrcodelable.text() == "" or self.ch4_qrcodelable.text() == "" or self.ch5_qrcodelable.text() == "" or self.ch6_qrcodelable.text() == "" or self.ch7_qrcodelable.text() == "" or self.ch8_qrcodelable.text() == "":
            QtWidgets.QMessageBox.warning(self, u"存取失敗", u"Qrcode未掃", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
            print("Qrcode未掃")
        else:
            QtWidgets.QMessageBox.information(self, u"存取成功", u"已成功另存Excel檔案", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)

            self.save_excel = pd.DataFrame({"Qrcode": [self.qrcode_result1[0], self.qrcode_result2[0],
                                                       self.qrcode_result3[0], self.qrcode_result4[0],
                                                       self.qrcode_result5[0], self.qrcode_result6[0],
                                                       self.qrcode_result7[0], self.qrcode_result8[0]],
                                            "T_On": [self.CH_T_On[0], self.CH_T_On[1], self.CH_T_On[2], self.CH_T_On[3],
                                                     self.CH_T_On[4], self.CH_T_On[5], self.CH_T_On[6],
                                                     self.CH_T_On[7]],
                                            "T_Off": [self.CH_T_Off[0], self.CH_T_Off[1], self.CH_T_Off[2],
                                                      self.CH_T_Off[3], self.CH_T_Off[4], self.CH_T_Off[5],
                                                      self.CH_T_Off[6], self.CH_T_Off[7]],
                                            "Slope" :[self.CH_slot[0], self.CH_slot[1], self.CH_slot[2],
                                                      self.CH_slot[3],self.CH_slot[4], self.CH_slot[5],
                                                      self.CH_slot[6], self.CH_slot[7]],
                                            "檢測結果": [self.TF_array[0], self.TF_array[1], self.TF_array[2],
                                                     self.TF_array[3],
                                                     self.TF_array[4], self.TF_array[5], self.TF_array[6],
                                                     self.TF_array[7]],
                                            "操作人員": [self.input_name.text(), "", "", "", "", "", "", ""],
                                            "檔案來源": [self.fname[0], "", "", "", "", "", "", ""]
                                            }, index=['CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8'])
            self.save_excel.to_excel('./result/history' + now_output_time+"output.xlsx", encoding="utf_8_sig")
            print("儲存成功")
    def clean_log(self):
        # T_On全關
        self.ch1_T_On.setText("")
        self.ch2_T_On.setText("")
        self.ch3_T_On.setText("")
        self.ch4_T_On.setText("")
        self.ch5_T_On.setText("")
        self.ch6_T_On.setText("")
        self.ch7_T_On.setText("")
        self.ch8_T_On.setText("")
        # T_Off全關
        self.ch1_T_Off.setText("")
        self.ch2_T_Off.setText("")
        self.ch3_T_Off.setText("")
        self.ch4_T_Off.setText("")
        self.ch5_T_Off.setText("")
        self.ch6_T_Off.setText("")
        self.ch7_T_Off.setText("")
        self.ch8_T_Off.setText("")
        # PF全關
        self.ch1_PF.setText("")
        self.ch2_PF.setText("")
        self.ch3_PF.setText("")
        self.ch4_PF.setText("")
        self.ch5_PF.setText("")
        self.ch6_PF.setText("")
        self.ch7_PF.setText("")
        self.ch8_PF.setText("")
        # 欄位
        self.input_file.setText("")
        self.input_name.setText("")
        # Slope
        self.ch1_slope.setText("")
        self.ch2_slope.setText("")
        self.ch3_slope.setText("")
        self.ch4_slope.setText("")
        self.ch5_slope.setText("")
        self.ch6_slope.setText("")
        self.ch7_slope.setText("")
        self.ch8_slope.setText("")
        # #Chart
        self.ch1_chart.setScene(None)
        self.ch2_chart.setScene(None)
        self.ch3_chart.setScene(None)
        self.ch4_chart.setScene(None)
        self.ch5_chart.setScene(None)
        self.ch6_chart.setScene(None)
        self.ch7_chart.setScene(None)
        self.ch8_chart.setScene(None)
    
    def take_com_picture(self):
        # ---------------CH1---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH1_data, 'o-', color='red', label="CH1_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH1.jpg')
        # ---------------CH2---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH2_data, 'o-', color='orange', label="CH2_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH2.jpg')
        # ---------------CH3---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH3_data, 'o-', color='yellow', label="CH3_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH3.jpg')
        # ---------------CH4---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH4_data, 'o-', color='green', label="CH4_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH4.jpg')
        # ---------------CH5---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH5_data, 'o-', color='#6F00FF', label="CH5_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH5.jpg')
        # ---------------CH6---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH6_data, 'o-', color='m', label="CH6_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH6.jpg')
        # ---------------CH7---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH7_data, 'o-', color='purple', label="CH7_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH7.jpg')
        # ---------------CH8---------------------
        plt.figure(figsize=(3, 3), dpi=60, linewidth=0)
        plt.plot(self.CH_total, self.CH8_data, 'o-', color='k', label="CH8_data")  # 紅
        plt.xlim(0, len(self.df.index))  # 設定圖範圍
        plt.ylim(0, 130)  # 設定圖範圍
        plt.savefig('image/CH8.jpg')

    def com_csv(self):
        self.com_A1_data = []
        self.com_A2_data = []
        self.com_A3_data = []
        self.com_A4_data = []
        self.com_A5_data = []
        self.com_A6_data = []
        self.com_A7_data = []
        self.com_A8_data = []
        self.com_B1_data = []
        self.com_B2_data = []
        self.com_B3_data = []
        self.com_B4_data = []
        self.com_B5_data = []
        self.com_B6_data = []
        self.com_B7_data = []
        self.com_B8_data = []
        self.temp_lid = []
        self.temp_well = []
        self.com_total = []
        #輸入ip位置
        self.fname_ip = self.com_IP.text()
        
        if(self.fname_ip == ""):
            print("沒有檔案")
        else:
            #創建資料夾
            if not os.path.isdir('./EGGI_COM'):
                os.mkdir('./EGGI_COM')
                if not os.path.isdir('./EGGI_COM/excel'):
                    os.mkdir('./EGGI_COM/excel')
                if not os.path.isdir('./EGGI_COM/roi'):
                    os.mkdir('./EGGI_COM/roi')
            os.system("scp pi@"+ str(self.fname_ip) + ":/home/pi/socket_cam/result/factory.csv ./EGGI_COM" )
            os.system("scp pi@"+ str(self.fname_ip) + ":/home/pi/socket_cam/para/ROIs/merge_finish_test.png ./EGGI_COM/roi")
            self.com_ROI.text = self.com_ID.text()
            self.com_ROI.setText(self.com_ROI.text)
            os.rename("./EGGI_COM/roi/merge_finish_test.png","./EGGI_COM/roi/" + str(self.com_ROI.text) +".png")
            #開始做資料運算
            self.com_file_csv = pd.read_csv("./EGGI_COM/factory.csv")
            print("-"*100)
            print(self.com_file_csv)
            for i in range(0,len(self.com_file_csv.index),1):
                self.temp_lid.append(self.com_file_csv.loc[i, 'temp_lid'])
                self.temp_well.append(self.com_file_csv.loc[i, 'temp_well'])
            for i in range(0,len(self.com_file_csv.index),1):
                self.com_total.append(i)
            print("-"*100)
            #Well槽平均
            self.well_pf_result = []
            self.temp_pf_result = []
            self.temp_well_average = np.mean(self.temp_well)
            #判斷Pass或Fail
            if(62>self.temp_well_average>60):
                self.well_pf_com_value.setText("Pass")
                self.well_pf_result.append("Pass")
            else:
                self.well_pf_com_value.setText("Fail")
                self.well_pf_result.append("Fail")
            self.well_com_value.setText(str(round(self.temp_well_average,2))) #取小數後第二位
            #上蓋平均
            self.temp_lid_average = np.mean(self.temp_lid)
            if (100>self.temp_lid_average > 90):
                self.top_pf_com_value.setText("Pass")
                self.temp_pf_result.append("Pass")
            else:
                self.top_pf_com_value.setText("Fail")
                self.temp_pf_result.append("Fail")
            self.top_com_value.setText(str(round(self.temp_lid_average,2))) #取小數後第二位

            print(self.temp_lid)
            print(self.temp_well)
            self.com_csv_chart()
            # 取圖片
            img = cv2.imread("EGGI_COM/temp_well.jpg")
            img2 = cv2.imread("EGGI_COM/temp_lid.jpg")

            # 轉換影象通道
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

            # 獲取影象大小
            x = img.shape[1]
            y = img.shape[0]
            x2 = img2.shape[1]
            y2 = img2.shape[0]

            # 圖片放縮尺度
            # self.zoomscale = 1
            frame = QImage(img, x, y, x * 3, QImage.Format_RGB888)
            self.pix = QPixmap.fromImage(frame)
            frame2 = QImage(img2, x2, y2, x2 * 3, QImage.Format_RGB888)
            self.pix2 = QPixmap.fromImage(frame2)

            # 建立畫素圖元
            self.item = QGraphicsPixmapItem(self.pix)
            self.item2 = QGraphicsPixmapItem(self.pix2)

            # 建立場景
            self.scene = QGraphicsScene()
            self.scene2 = QGraphicsScene()
            self.scene.addItem(self.item)
            self.scene2.addItem(self.item2)

            # 將場景新增至檢視
            self.well_com_chart.setScene(self.scene)
            self.top_com_chart.setScene(self.scene2)

    
    def com_csv_chart(self):
        # ---------------temp_lid---------------------
        plt.figure(figsize=(5, 3), dpi=100, linewidth=0)
        plt.plot(self.com_total, self.temp_lid, 'o-', color='red', label="temp_lid")  # 紅
        plt.xlim(0, len(self.com_file_csv.index))   # 設定x軸圖範圍
        plt.ylim(70, 105)
        plt.savefig('EGGI_COM/temp_lid.jpg')
        # ---------------temp_well---------------------
        plt.figure(figsize=(5, 3), dpi=100, linewidth=0)
        plt.plot(self.com_total, self.temp_well, 'o-', color='blue', label="temp_well")  # 紅
        plt.xlim(0, len(self.com_file_csv.index))   # 設定x軸圖範圍 
        plt.ylim(30, 70)
        plt.savefig('EGGI_COM/temp_well.jpg')
    
    def com_save(self):
        if self.com_IP.text() == "" or self.com_ID.text() == "":
            QtWidgets.QMessageBox.critical(self, u"存取失敗", u"請輸入操作人員", buttons=QtWidgets.QMessageBox.Ok,
                                    defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            if os.path.isfile('./EGGI_COM/excel/eggi_temp_' + com_now_output +"output.xlsx"):
                new_df = pd.read_excel(r"./EGGI_COM/excel/eggi_temp_" + com_now_output + "output.xlsx", index_col=0)
                print("-"*100)
                # print("test")
                new_data = pd.DataFrame([[self.com_ID.text(),self.com_IP.text(),str(round(self.temp_well_average,2)),
                                         self.well_pf_result,str(round(self.temp_lid_average,2)),self.temp_pf_result]],
                                         columns=["ID", "eGGi IP", "Well槽","Well Pass/Fail","上蓋","上蓋 Pass/Fail"])
                self.save_excel = new_df.append(new_data, ignore_index=True)
                print(new_df)
                self.save_excel.to_excel(r'./EGGI_COM/excel/eggi_temp_' + com_now_output +"output.xlsx",encoding="utf_8_sig")
            else:
                QtWidgets.QMessageBox.information(self, u"存取成功", u"已成功另存Excel檔案", buttons=QtWidgets.QMessageBox.Ok,
                                            defaultButton=QtWidgets.QMessageBox.Ok)
                self.save_excel = pd.DataFrame({"ID": [self.com_ID.text()],
                                                "eGGi IP": [self.com_IP.text()],
                                                "Well槽": [str(round(self.temp_well_average,2))],
                                                "Well Pass/Fail": [self.well_pf_result],
                                                "上蓋": [str(round(self.temp_lid_average,2))],
                                                "上蓋 Pass/Fail" :[self.temp_pf_result],
                                                "eGGi IP": [self.com_IP.text()]
                                                })

                self.save_excel.to_excel('./EGGI_COM/excel/eggi_temp_' + com_now_output +"output.xlsx",encoding="utf_8_sig")

    def com_clean(self):
        self.well_com_value.setText("")
        self.well_pf_com_value.setText("")
        self.top_com_value.setText("")
        self.com_IP.setText("")
        self.com_ID.setText("")
        self.top_pf_com_value.setText("")
        self.com_ROI.setText("")
        self.well_com_chart.setScene(None)
        self.top_com_chart.setScene(None)

    def com_id_qrcode(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.com_ID.setText(text)
                # self.qrcode_result1.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        self.qrcode_result1.append("None")
        cv2.destroyAllWindows()
    
    def com_roi_rename(self):
        self.roi_rename = self.com_ROI.text()
        if self.com_ROI.text() == "":
            QtWidgets.QMessageBox.critical(self, u"警告", u"請輸入更改檔名", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        if not os.path.isfile('./EGGI_COM/merge_finish_test.png'):
            QtWidgets.QMessageBox.critical(self, u"警告", u"merge_finish_test.png不存在", buttons=QtWidgets.QMessageBox.Ok,
                                          defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            os.rename("./EGGI_COM/merge_finish_test.png","./EGGI_COM/" + self.roi_rename +".png")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 84, 1131, 739))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Sulink = QtWidgets.QWidget()
        self.tab_Sulink.setObjectName("tab_Sulink")
        self.Input_box = QtWidgets.QGroupBox(self.tab_Sulink)
        self.Input_box.setGeometry(QtCore.QRect(0, 6, 531, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Input_box.setFont(font)
        self.Input_box.setStyleSheet("QGroupBox {\n"
"            border-color: rgb(156, 156, 156);\n"
"        }")
        self.Input_box.setObjectName("Input_box")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.Input_box)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_file = QtWidgets.QLineEdit(self.Input_box)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(False)
        self.input_file.setFont(font)
        self.input_file.setObjectName("input_file")
        self.gridLayout_2.addWidget(self.input_file, 1, 1, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.Input_box)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_2.addWidget(self.btn_save, 1, 2, 1, 1)
        self.input_name = QtWidgets.QLineEdit(self.Input_box)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(False)
        self.input_name.setFont(font)
        self.input_name.setObjectName("input_name")
        self.gridLayout_2.addWidget(self.input_name, 0, 1, 1, 1)
        self.label_txt_2 = QtWidgets.QLabel(self.Input_box)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_txt_2.setFont(font)
        self.label_txt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt_2.setObjectName("label_txt_2")
        self.gridLayout_2.addWidget(self.label_txt_2, 1, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.Input_box)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.btn_opentxt = QtWidgets.QPushButton(self.Input_box)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.btn_opentxt.setFont(font)
        self.btn_opentxt.setObjectName("btn_opentxt")
        self.gridLayout_2.addWidget(self.btn_opentxt, 0, 2, 1, 1)
        self.btn_clean = QtWidgets.QPushButton(self.Input_box)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_clean.setFont(font)
        self.btn_clean.setObjectName("btn_clean")
        self.gridLayout_2.addWidget(self.btn_clean, 2, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.Chart_box = QtWidgets.QGroupBox(self.tab_Sulink)
        self.Chart_box.setGeometry(QtCore.QRect(0, 192, 531, 391))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Chart_box.setFont(font)
        self.Chart_box.setObjectName("Chart_box")
        self.splitter_2 = QtWidgets.QSplitter(self.Chart_box)
        self.splitter_2.setGeometry(QtCore.QRect(16, 156, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.widget_6 = QtWidgets.QWidget(self.splitter_2)
        self.widget_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.widget_7 = QtWidgets.QWidget(self.splitter_2)
        self.widget_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_7.setObjectName("widget_7")
        self.widget_8 = QtWidgets.QWidget(self.splitter_2)
        self.widget_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_8.setObjectName("widget_8")
        self.widget_5 = QtWidgets.QWidget(self.splitter_2)
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Chart_box)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 511, 349))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ch6_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch6_chart.setObjectName("ch6_chart")
        self.gridLayout_3.addWidget(self.ch6_chart, 2, 1, 1, 1)
        self.ch6_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch6_display.setFont(font)
        self.ch6_display.setObjectName("ch6_display")
        self.gridLayout_3.addWidget(self.ch6_display, 3, 1, 1, 1)
        self.ch4_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch4_chart.setObjectName("ch4_chart")
        self.gridLayout_3.addWidget(self.ch4_chart, 0, 3, 1, 1)
        self.ch5_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch5_chart.setObjectName("ch5_chart")
        self.gridLayout_3.addWidget(self.ch5_chart, 2, 0, 1, 1)
        self.ch2_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch2_chart.setObjectName("ch2_chart")
        self.gridLayout_3.addWidget(self.ch2_chart, 0, 1, 1, 1)
        self.ch3_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch3_chart.setObjectName("ch3_chart")
        self.gridLayout_3.addWidget(self.ch3_chart, 0, 2, 1, 1)
        self.ch8_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch8_display.setFont(font)
        self.ch8_display.setObjectName("ch8_display")
        self.gridLayout_3.addWidget(self.ch8_display, 3, 3, 1, 1)
        self.ch7_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch7_chart.setObjectName("ch7_chart")
        self.gridLayout_3.addWidget(self.ch7_chart, 2, 2, 1, 1)
        self.ch1_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch1_chart.setObjectName("ch1_chart")
        self.gridLayout_3.addWidget(self.ch1_chart, 0, 0, 1, 1)
        self.ch7_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch7_display.setFont(font)
        self.ch7_display.setObjectName("ch7_display")
        self.gridLayout_3.addWidget(self.ch7_display, 3, 2, 1, 1)
        self.ch8_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch8_chart.setObjectName("ch8_chart")
        self.gridLayout_3.addWidget(self.ch8_chart, 2, 3, 1, 1)
        self.ch5_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch5_display.setFont(font)
        self.ch5_display.setObjectName("ch5_display")
        self.gridLayout_3.addWidget(self.ch5_display, 3, 0, 1, 1)
        self.ch4_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch4_display.setFont(font)
        self.ch4_display.setObjectName("ch4_display")
        self.gridLayout_3.addWidget(self.ch4_display, 1, 3, 1, 1)
        self.ch3_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch3_display.setFont(font)
        self.ch3_display.setObjectName("ch3_display")
        self.gridLayout_3.addWidget(self.ch3_display, 1, 2, 1, 1)
        self.ch2_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_display.setFont(font)
        self.ch2_display.setObjectName("ch2_display")
        self.gridLayout_3.addWidget(self.ch2_display, 1, 1, 1, 1)
        self.ch1_display = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_display.setFont(font)
        self.ch1_display.setObjectName("ch1_display")
        self.gridLayout_3.addWidget(self.ch1_display, 1, 0, 1, 1)
        self.Result_box = QtWidgets.QGroupBox(self.tab_Sulink)
        self.Result_box.setGeometry(QtCore.QRect(540, 6, 581, 571))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Result_box.setFont(font)
        self.Result_box.setObjectName("Result_box")
        self.layoutWidget = QtWidgets.QWidget(self.Result_box)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 42, 561, 349))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ch3_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch3_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.gridLayout.addWidget(self.ch3_T_On, 3, 3, 1, 1)
        self.ch5_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch5_qrcode.setFont(font)
        self.ch5_qrcode.setObjectName("ch5_qrcode")
        self.gridLayout.addWidget(self.ch5_qrcode, 5, 1, 1, 1)
        self.ch3_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch3_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_PF.setObjectName("ch3_PF")
        self.gridLayout.addWidget(self.ch3_PF, 3, 6, 1, 1)
        self.ch5_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_PF.setObjectName("ch5_PF")
        self.gridLayout.addWidget(self.ch5_PF, 5, 6, 1, 1)
        self.ch8_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_qrcodelable.setObjectName("ch8_qrcodelable")
        self.gridLayout.addWidget(self.ch8_qrcodelable, 8, 2, 1, 1)
        self.ch8_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_slope.setObjectName("ch8_slope")
        self.gridLayout.addWidget(self.ch8_slope, 8, 5, 1, 1)
        self.ch7_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.gridLayout.addWidget(self.ch7_T_Off, 7, 4, 1, 1)
        self.label_ch3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch3.setFont(font)
        self.label_ch3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch3.setObjectName("label_ch3")
        self.gridLayout.addWidget(self.label_ch3, 3, 0, 1, 1)
        self.ch5_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_slope.setObjectName("ch5_slope")
        self.gridLayout.addWidget(self.ch5_slope, 5, 5, 1, 1)
        self.ch4_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch4_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.gridLayout.addWidget(self.ch4_T_Off, 4, 4, 1, 1)
        self.ch1_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ch1_qrcodelable.setFont(font)
        self.ch1_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_qrcodelable.setObjectName("ch1_qrcodelable")
        self.gridLayout.addWidget(self.ch1_qrcodelable, 1, 2, 1, 1)
        self.label_qrcode = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_qrcode.setFont(font)
        self.label_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode.setObjectName("label_qrcode")
        self.gridLayout.addWidget(self.label_qrcode, 0, 2, 1, 1)
        self.label_ch8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch8.setFont(font)
        self.label_ch8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch8.setObjectName("label_ch8")
        self.gridLayout.addWidget(self.label_ch8, 8, 0, 1, 1)
        self.ch6_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.gridLayout.addWidget(self.ch6_T_Off, 6, 4, 1, 1)
        self.label_ch7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch7.setFont(font)
        self.label_ch7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch7.setObjectName("label_ch7")
        self.gridLayout.addWidget(self.label_ch7, 7, 0, 1, 1)
        self.ch8_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_PF.setObjectName("ch8_PF")
        self.gridLayout.addWidget(self.ch8_PF, 8, 6, 1, 1)
        self.ch4_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch4_qrcode.setFont(font)
        self.ch4_qrcode.setObjectName("ch4_qrcode")
        self.gridLayout.addWidget(self.ch4_qrcode, 4, 1, 1, 1)
        self.ch2_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ch2_qrcodelable.setFont(font)
        self.ch2_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_qrcodelable.setObjectName("ch2_qrcodelable")
        self.gridLayout.addWidget(self.ch2_qrcodelable, 2, 2, 1, 1)
        self.ch4_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch4_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.gridLayout.addWidget(self.ch4_T_On, 4, 3, 1, 1)
        self.label_T_On = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_T_On.setFont(font)
        self.label_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On.setObjectName("label_T_On")
        self.gridLayout.addWidget(self.label_T_On, 0, 3, 1, 1)
        self.label_ch1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch1.setFont(font)
        self.label_ch1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch1.setObjectName("label_ch1")
        self.gridLayout.addWidget(self.label_ch1, 1, 0, 1, 1)
        self.label_ch5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch5.setFont(font)
        self.label_ch5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch5.setObjectName("label_ch5")
        self.gridLayout.addWidget(self.label_ch5, 5, 0, 1, 1)
        self.ch2_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch2_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_PF.setObjectName("ch2_PF")
        self.gridLayout.addWidget(self.ch2_PF, 2, 6, 1, 1)
        self.label_ch2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch2.setFont(font)
        self.label_ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch2.setObjectName("label_ch2")
        self.gridLayout.addWidget(self.label_ch2, 2, 0, 1, 1)
        self.ch3_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch3_qrcode.setFont(font)
        self.ch3_qrcode.setObjectName("ch3_qrcode")
        self.gridLayout.addWidget(self.ch3_qrcode, 3, 1, 1, 1)
        self.ch4_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch4_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_slope.setObjectName("ch4_slope")
        self.gridLayout.addWidget(self.ch4_slope, 4, 5, 1, 1)
        self.ch8_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch8_qrcode.setFont(font)
        self.ch8_qrcode.setObjectName("ch8_qrcode")
        self.gridLayout.addWidget(self.ch8_qrcode, 8, 1, 1, 1)
        self.ch6_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_slope.setObjectName("ch6_slope")
        self.gridLayout.addWidget(self.ch6_slope, 6, 5, 1, 1)
        self.ch1_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch1_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_slope.setObjectName("ch1_slope")
        self.gridLayout.addWidget(self.ch1_slope, 1, 5, 1, 1)
        self.ch2_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch2_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.gridLayout.addWidget(self.ch2_T_On, 2, 3, 1, 1)
        self.ch3_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ch3_qrcodelable.setFont(font)
        self.ch3_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_qrcodelable.setObjectName("ch3_qrcodelable")
        self.gridLayout.addWidget(self.ch3_qrcodelable, 3, 2, 1, 1)
        self.label_ch4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch4.setFont(font)
        self.label_ch4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch4.setObjectName("label_ch4")
        self.gridLayout.addWidget(self.label_ch4, 4, 0, 1, 1)
        self.ch2_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch2_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.gridLayout.addWidget(self.ch2_T_Off, 2, 4, 1, 1)
        self.ch2_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch2_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_slope.setObjectName("ch2_slope")
        self.gridLayout.addWidget(self.ch2_slope, 2, 5, 1, 1)
        self.ch1_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch1_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.gridLayout.addWidget(self.ch1_T_On, 1, 3, 1, 1)
        self.label_ch6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_ch6.setFont(font)
        self.label_ch6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch6.setObjectName("label_ch6")
        self.gridLayout.addWidget(self.label_ch6, 6, 0, 1, 1)
        self.ch6_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_PF.setObjectName("ch6_PF")
        self.gridLayout.addWidget(self.ch6_PF, 6, 6, 1, 1)
        self.ch3_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch3_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.gridLayout.addWidget(self.ch3_T_Off, 3, 4, 1, 1)
        self.ch4_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ch4_qrcodelable.setFont(font)
        self.ch4_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_qrcodelable.setObjectName("ch4_qrcodelable")
        self.gridLayout.addWidget(self.ch4_qrcodelable, 4, 2, 1, 1)
        self.ch7_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_qrcodelable.setObjectName("ch7_qrcodelable")
        self.gridLayout.addWidget(self.ch7_qrcodelable, 7, 2, 1, 1)
        self.ch5_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.gridLayout.addWidget(self.ch5_T_On, 5, 3, 1, 1)
        self.ch5_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.gridLayout.addWidget(self.ch5_T_Off, 5, 4, 1, 1)
        self.ch6_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_qrcodelable.setObjectName("ch6_qrcodelable")
        self.gridLayout.addWidget(self.ch6_qrcodelable, 6, 2, 1, 1)
        self.label_T_Off = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_T_Off.setFont(font)
        self.label_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_Off.setObjectName("label_T_Off")
        self.gridLayout.addWidget(self.label_T_Off, 0, 4, 1, 1)
        self.ch7_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch7_qrcode.setFont(font)
        self.ch7_qrcode.setObjectName("ch7_qrcode")
        self.gridLayout.addWidget(self.ch7_qrcode, 7, 1, 1, 1)
        self.ch5_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_qrcodelable.setObjectName("ch5_qrcodelable")
        self.gridLayout.addWidget(self.ch5_qrcodelable, 5, 2, 1, 1)
        self.label_Slope = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_Slope.setFont(font)
        self.label_Slope.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Slope.setObjectName("label_Slope")
        self.gridLayout.addWidget(self.label_Slope, 0, 5, 1, 1)
        self.ch8_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_T_Off.setObjectName("ch8_T_Off")
        self.gridLayout.addWidget(self.ch8_T_Off, 8, 4, 1, 1)
        self.label_qrcode_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_qrcode_3.setFont(font)
        self.label_qrcode_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode_3.setObjectName("label_qrcode_3")
        self.gridLayout.addWidget(self.label_qrcode_3, 0, 1, 1, 1)
        self.ch1_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch1_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_PF.setObjectName("ch1_PF")
        self.gridLayout.addWidget(self.ch1_PF, 1, 6, 1, 1)
        self.ch6_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.gridLayout.addWidget(self.ch6_T_On, 6, 3, 1, 1)
        self.ch1_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch1_qrcode.setFont(font)
        self.ch1_qrcode.setObjectName("ch1_qrcode")
        self.gridLayout.addWidget(self.ch1_qrcode, 1, 1, 1, 1)
        self.ch6_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch6_qrcode.setFont(font)
        self.ch6_qrcode.setObjectName("ch6_qrcode")
        self.gridLayout.addWidget(self.ch6_qrcode, 6, 1, 1, 1)
        self.label_T_On_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_T_On_14.setFont(font)
        self.label_T_On_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On_14.setObjectName("label_T_On_14")
        self.gridLayout.addWidget(self.label_T_On_14, 0, 6, 1, 1)
        self.ch7_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_slope.setObjectName("ch7_slope")
        self.gridLayout.addWidget(self.ch7_slope, 7, 5, 1, 1)
        self.ch4_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch4_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_PF.setObjectName("ch4_PF")
        self.gridLayout.addWidget(self.ch4_PF, 4, 6, 1, 1)
        self.ch7_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.gridLayout.addWidget(self.ch7_T_On, 7, 3, 1, 1)
        self.ch8_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_T_On.setObjectName("ch8_T_On")
        self.gridLayout.addWidget(self.ch8_T_On, 8, 3, 1, 1)
        self.ch1_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch1_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.gridLayout.addWidget(self.ch1_T_Off, 1, 4, 1, 1)
        self.ch2_qrcode = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ch2_qrcode.setFont(font)
        self.ch2_qrcode.setObjectName("ch2_qrcode")
        self.gridLayout.addWidget(self.ch2_qrcode, 2, 1, 1, 1)
        self.ch3_slope = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch3_slope.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_slope.setObjectName("ch3_slope")
        self.gridLayout.addWidget(self.ch3_slope, 3, 5, 1, 1)
        self.ch7_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_PF.setObjectName("ch7_PF")
        self.gridLayout.addWidget(self.ch7_PF, 7, 6, 1, 1)
        self.tabWidget.addTab(self.tab_Sulink, "")
        self.tab_hardware = QtWidgets.QWidget()
        self.tab_hardware.setObjectName("tab_hardware")
        self.Chart_box_com = QtWidgets.QGroupBox(self.tab_hardware)
        self.Chart_box_com.setGeometry(QtCore.QRect(1, 205, 531, 385))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Chart_box_com.setFont(font)
        self.Chart_box_com.setObjectName("Chart_box_com")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Chart_box_com)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.well_com_chart = QtWidgets.QGraphicsView(self.Chart_box_com)
        self.well_com_chart.setObjectName("well_com_chart")
        self.gridLayout_4.addWidget(self.well_com_chart, 2, 1, 1, 1)
        self.Input_box_com = QtWidgets.QGroupBox(self.tab_hardware)
        self.Input_box_com.setGeometry(QtCore.QRect(0, 6, 531, 199))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Input_box_com.setFont(font)
        self.Input_box_com.setStyleSheet("QGroupBox {\n"
"            border-color: rgb(156, 156, 156);\n"
"        }")
        self.Input_box_com.setObjectName("Input_box_com")
        self.layoutWidget1 = QtWidgets.QWidget(self.Input_box_com)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 31, 511, 103))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.com_IP = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(False)
        self.com_IP.setFont(font)
        self.com_IP.setObjectName("com_IP")
        self.gridLayout_6.addWidget(self.com_IP, 1, 1, 1, 1)
        self.btn_opentxt_com = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.btn_opentxt_com.setFont(font)
        self.btn_opentxt_com.setObjectName("btn_opentxt_com")
        self.gridLayout_6.addWidget(self.btn_opentxt_com, 1, 2, 1, 1)
        self.IP_name_com = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.IP_name_com.setFont(font)
        self.IP_name_com.setAlignment(QtCore.Qt.AlignCenter)
        self.IP_name_com.setObjectName("IP_name_com")
        self.gridLayout_6.addWidget(self.IP_name_com, 1, 0, 1, 1)
        self.ID_name_com = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.ID_name_com.setFont(font)
        self.ID_name_com.setAlignment(QtCore.Qt.AlignCenter)
        self.ID_name_com.setObjectName("ID_name_com")
        self.gridLayout_6.addWidget(self.ID_name_com, 0, 0, 1, 1)
        self.com_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(False)
        self.com_ID.setFont(font)
        self.com_ID.setObjectName("com_ID")
        self.gridLayout_6.addWidget(self.com_ID, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.Input_box_com)
        self.layoutWidget2.setGeometry(QtCore.QRect(90, 138, 331, 44))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.btn_save_com = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_save_com.setFont(font)
        self.btn_save_com.setStyleSheet("color: rgb(0, 170, 0);")
        self.btn_save_com.setObjectName("btn_save_com")
        self.gridLayout_9.addWidget(self.btn_save_com, 0, 0, 1, 1)
        self.btn_clean_com = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_clean_com.setFont(font)
        self.btn_clean_com.setStyleSheet("color: rgb(255, 255, 0);\n"
"color: rgb(255, 170, 0);")
        self.btn_clean_com.setObjectName("btn_clean_com")
        self.gridLayout_9.addWidget(self.btn_clean_com, 0, 1, 1, 1)
        self.Result_box_com = QtWidgets.QGroupBox(self.tab_hardware)
        self.Result_box_com.setGeometry(QtCore.QRect(540, 6, 571, 205))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Result_box_com.setFont(font)
        self.Result_box_com.setObjectName("Result_box_com")
        self.layoutWidget_7 = QtWidgets.QWidget(self.Result_box_com)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 30, 541, 75))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.top_pf_com_value = QtWidgets.QLineEdit(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.top_pf_com_value.setFont(font)
        self.top_pf_com_value.setAlignment(QtCore.Qt.AlignCenter)
        self.top_pf_com_value.setObjectName("top_pf_com_value")
        self.gridLayout_7.addWidget(self.top_pf_com_value, 1, 4, 1, 1)
        self.well_pf_com = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.well_pf_com.setFont(font)
        self.well_pf_com.setAlignment(QtCore.Qt.AlignCenter)
        self.well_pf_com.setObjectName("well_pf_com")
        self.gridLayout_7.addWidget(self.well_pf_com, 0, 2, 1, 1)
        self.well_com_value = QtWidgets.QLineEdit(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.well_com_value.setFont(font)
        self.well_com_value.setAlignment(QtCore.Qt.AlignCenter)
        self.well_com_value.setObjectName("well_com_value")
        self.gridLayout_7.addWidget(self.well_com_value, 1, 1, 1, 1)
        self.label_step = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_step.setFont(font)
        self.label_step.setAlignment(QtCore.Qt.AlignCenter)
        self.label_step.setObjectName("label_step")
        self.gridLayout_7.addWidget(self.label_step, 1, 0, 1, 1)
        self.top_com = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.top_com.setFont(font)
        self.top_com.setAlignment(QtCore.Qt.AlignCenter)
        self.top_com.setObjectName("top_com")
        self.gridLayout_7.addWidget(self.top_com, 0, 3, 1, 1)
        self.top_pf_com = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.top_pf_com.setFont(font)
        self.top_pf_com.setAlignment(QtCore.Qt.AlignCenter)
        self.top_pf_com.setObjectName("top_pf_com")
        self.gridLayout_7.addWidget(self.top_pf_com, 0, 4, 1, 1)
        self.well_pf_com_value = QtWidgets.QLineEdit(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.well_pf_com_value.setFont(font)
        self.well_pf_com_value.setAlignment(QtCore.Qt.AlignCenter)
        self.well_pf_com_value.setObjectName("well_pf_com_value")
        self.gridLayout_7.addWidget(self.well_pf_com_value, 1, 2, 1, 1)
        self.top_com_value = QtWidgets.QLineEdit(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.top_com_value.setFont(font)
        self.top_com_value.setAlignment(QtCore.Qt.AlignCenter)
        self.top_com_value.setObjectName("top_com_value")
        self.gridLayout_7.addWidget(self.top_com_value, 1, 3, 1, 1)
        self.well_com = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.well_com.setFont(font)
        self.well_com.setAlignment(QtCore.Qt.AlignCenter)
        self.well_com.setObjectName("well_com")
        self.gridLayout_7.addWidget(self.well_com, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.Result_box_com)
        self.widget.setGeometry(QtCore.QRect(10, 120, 541, 44))
        self.widget.setObjectName("widget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.com_ROI = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.com_ROI.setFont(font)
        self.com_ROI.setObjectName("com_ROI")
        self.gridLayout_11.addWidget(self.com_ROI, 0, 1, 1, 1)
        self.ROI_name_com = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.ROI_name_com.setFont(font)
        self.ROI_name_com.setAlignment(QtCore.Qt.AlignCenter)
        self.ROI_name_com.setObjectName("ROI_name_com")
        self.gridLayout_11.addWidget(self.ROI_name_com, 0, 0, 1, 1)
        self.Chart_box_com_2 = QtWidgets.QGroupBox(self.tab_hardware)
        self.Chart_box_com_2.setGeometry(QtCore.QRect(540, 204, 571, 385))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Chart_box_com_2.setFont(font)
        self.Chart_box_com_2.setObjectName("Chart_box_com_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Chart_box_com_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.top_com_chart = QtWidgets.QGraphicsView(self.Chart_box_com_2)
        self.top_com_chart.setObjectName("top_com_chart")
        self.gridLayout_8.addWidget(self.top_com_chart, 0, 0, 2, 2)
        self.tabWidget.addTab(self.tab_hardware, "")
        self.EGGI_Title = QtWidgets.QLabel(self.centralwidget)
        self.EGGI_Title.setGeometry(QtCore.QRect(0, 0, 1131, 85))
        font = QtGui.QFont()
        font.setPointSize(38)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.EGGI_Title.setFont(font)
        self.EGGI_Title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.EGGI_Title.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.EGGI_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EGGI_Title.setObjectName("EGGI_Title")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_clean.clicked.connect(self.clean_log)
        self.btn_opentxt.clicked.connect(self.browsefile)
        self.btn_save.clicked.connect(self.save_log)
        self.ch1_qrcode.clicked.connect(self.qrcode1)
        self.ch2_qrcode.clicked.connect(self.qrcode2)
        self.ch3_qrcode.clicked.connect(self.qrcode3)
        self.ch4_qrcode.clicked.connect(self.qrcode4)
        self.ch5_qrcode.clicked.connect(self.qrcode5)
        self.ch6_qrcode.clicked.connect(self.qrcode6)
        self.ch7_qrcode.clicked.connect(self.qrcode7)
        self.ch8_qrcode.clicked.connect(self.qrcode8)
        self.ch1_display.clicked.connect(self.display1)
        self.ch2_display.clicked.connect(self.display2)
        self.ch3_display.clicked.connect(self.display3)
        self.ch4_display.clicked.connect(self.display4)
        self.ch5_display.clicked.connect(self.display5)
        self.ch6_display.clicked.connect(self.display6)
        self.ch7_display.clicked.connect(self.display7)
        self.ch8_display.clicked.connect(self.display8)
        self.input_name.text() #輸入操作人員
        self.btn_opentxt_com.clicked.connect(self.com_csv)
        self.btn_save_com.clicked.connect(self.com_save)
        self.btn_clean_com.clicked.connect(self.com_clean)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Input_box.setTitle(_translate("MainWindow", "Input"))
        self.btn_save.setText(_translate("MainWindow", "儲存"))
        self.label_txt_2.setText(_translate("MainWindow", "TXT檔案"))
        self.label_name.setText(_translate("MainWindow", "ID"))
        self.btn_opentxt.setText(_translate("MainWindow", "打開"))
        self.btn_clean.setText(_translate("MainWindow", "清除"))
        self.Chart_box.setTitle(_translate("MainWindow", "Chart"))
        self.ch6_display.setText(_translate("MainWindow", "顯示CH6"))
        self.ch8_display.setText(_translate("MainWindow", "顯示CH8"))
        self.ch7_display.setText(_translate("MainWindow", "顯示CH7"))
        self.ch5_display.setText(_translate("MainWindow", "顯示CH5"))
        self.ch4_display.setText(_translate("MainWindow", "顯示CH4"))
        self.ch3_display.setText(_translate("MainWindow", "顯示CH3"))
        self.ch2_display.setText(_translate("MainWindow", "顯示CH2"))
        self.ch1_display.setText(_translate("MainWindow", "顯示CH1"))
        self.Result_box.setTitle(_translate("MainWindow", "Result"))
        self.ch5_qrcode.setText(_translate("MainWindow", "檢測CH5"))
        self.label_ch3.setText(_translate("MainWindow", "CH3"))
        self.label_qrcode.setText(_translate("MainWindow", "QRCODE"))
        self.label_ch8.setText(_translate("MainWindow", "CH8"))
        self.label_ch7.setText(_translate("MainWindow", "CH7"))
        self.ch4_qrcode.setText(_translate("MainWindow", "檢測CH4"))
        self.label_T_On.setText(_translate("MainWindow", "T_On"))
        self.label_ch1.setText(_translate("MainWindow", "CH1"))
        self.label_ch5.setText(_translate("MainWindow", "CH5"))
        self.label_ch2.setText(_translate("MainWindow", "CH2"))
        self.ch3_qrcode.setText(_translate("MainWindow", "檢測CH3"))
        self.ch8_qrcode.setText(_translate("MainWindow", "檢測CH8"))
        self.label_ch4.setText(_translate("MainWindow", "CH4"))
        self.label_ch6.setText(_translate("MainWindow", "CH6"))
        self.label_T_Off.setText(_translate("MainWindow", "T_Off"))
        self.ch7_qrcode.setText(_translate("MainWindow", "檢測CH7"))
        self.label_Slope.setText(_translate("MainWindow", "Slope"))
        self.label_qrcode_3.setText(_translate("MainWindow", "READ"))
        self.ch1_qrcode.setText(_translate("MainWindow", "檢測CH1"))
        self.ch6_qrcode.setText(_translate("MainWindow", "檢測CH6"))
        self.label_T_On_14.setText(_translate("MainWindow", "P/F"))
        self.ch2_qrcode.setText(_translate("MainWindow", "檢測CH2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Sulink), _translate("MainWindow", "溫度保護器"))
        self.Chart_box_com.setTitle(_translate("MainWindow", "Well"))
        self.Input_box_com.setTitle(_translate("MainWindow", "Input"))
        self.btn_opentxt_com.setText(_translate("MainWindow", "連接"))
        self.IP_name_com.setText(_translate("MainWindow", "eGGi IP"))
        self.ID_name_com.setText(_translate("MainWindow", "ID"))
        self.btn_save_com.setText(_translate("MainWindow", "儲存"))
        self.btn_clean_com.setText(_translate("MainWindow", "重置"))
        self.Result_box_com.setTitle(_translate("MainWindow", "Result"))
        self.well_pf_com.setText(_translate("MainWindow", "Well P/F"))
        self.label_step.setText(_translate("MainWindow", "Step1"))
        self.top_com.setText(_translate("MainWindow", "上蓋"))
        self.top_pf_com.setText(_translate("MainWindow", "上蓋 P/F"))
        self.well_com.setText(_translate("MainWindow", "Well"))
        self.ROI_name_com.setText(_translate("MainWindow", "Merged ROI"))
        self.Chart_box_com_2.setTitle(_translate("MainWindow", "上蓋"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hardware), _translate("MainWindow", "EGGI主機"))
        self.EGGI_Title.setText(_translate("MainWindow", "溫度數據與ROI"))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())