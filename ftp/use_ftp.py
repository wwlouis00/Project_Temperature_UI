from ftplib import FTP
import os
import sys
import time
import socket


class MyFTP:
    def __init__(self, host, port=22):
        self.host = host
        self.port = port
        self.ftp = FTP()
        # 重新設定下編碼方式
        self.ftp.encoding = 'gbk'
        self.log_file = open("log.txt", "a")
        self.file_list = []

    def login(self, username, password):
        """ 初始化 FTP 客戶端
            引數:
                  username: 使用者名稱

                 password: 密碼
            """
        try:
            timeout = 60
            socket.setdefaulttimeout(timeout)
            # 0主動模式 1 #被動模式
            self.ftp.set_pasv(True)
            # 開啟除錯級別2，顯示詳細資訊
            # self.ftp.set_debuglevel(2)

            self.debug_print('開始嘗試連線到 %s' % self.host)
            self.ftp.connect(self.host, self.port)
            self.debug_print('成功連線到 %s' % self.host)

            self.debug_print('開始嘗試登入到 %s' % self.host)
            self.ftp.login(username, password)
            self.debug_print('成功登入到 %s' % self.host)

            self.debug_print(self.ftp.welcome)
        except Exception as err:
            self.deal_error("FTP 連線或登入失敗 ，錯誤描述為：%s" % err)
            pass

    def is_same_size(self, local_file, remote_file):
        """判斷遠端檔案和本地檔案大小是否一致

           引數:
             local_file: 本地檔案

             remote_file: 遠端檔案
        """
        try:
            remote_file_size = self.ftp.size(remote_file)
        except Exception as err:
            # self.debug_print("is_same_size() 錯誤描述為：%s" % err)
            remote_file_size = -1

        try:
            local_file_size = os.path.getsize(local_file)
        except Exception as err:
            # self.debug_print("is_same_size() 錯誤描述為：%s" % err)
            local_file_size = -1

        self.debug_print('local_file_size:%d  , remote_file_size:%d' % (local_file_size, remote_file_size))
        if remote_file_size == local_file_size:
            return 1
        else:
            return 0

    def download_file(self, local_file, remote_file):
        """從ftp下載檔案
            引數:
                local_file: 本地檔案

                remote_file: 遠端檔案
        """
        self.debug_print("download_file()---> local_path = %s ,remote_path = %s" % (local_file, remote_file))

        if self.is_same_size(local_file, remote_file):
            self.debug_print('%s 檔案大小相同，無需下載' % local_file)
            return
        else:
            try:
                self.debug_print('>>>>>>>>>>>>下載檔案 %s ... ...' % local_file)
                buf_size = 1024
                file_handler = open(local_file, 'wb')
                self.ftp.retrbinary('RETR %s' % remote_file, file_handler.write, buf_size)
                file_handler.close()
            except Exception as err:
                self.debug_print('下載檔案出錯，出現異常：%s ' % err)
                return

    def download_file_tree(self, local_path, remote_path):
        """從遠端目錄下載多個檔案到本地目錄
                       引數:
                         local_path: 本地路徑

                         remote_path: 遠端路徑
                """
        print("download_file_tree()--->  local_path = %s ,remote_path = %s" % (local_path, remote_path))
        try:
            self.ftp.cwd(remote_path)
        except Exception as err:
            self.debug_print('遠端目錄%s不存在，繼續...' % remote_path + " ,具體錯誤描述為：%s" % err)
            return

        if not os.path.isdir(local_path):
            self.debug_print('本地目錄%s不存在，先建立本地目錄' % local_path)
            os.makedirs(local_path)

        self.debug_print('切換至目錄: %s' % self.ftp.pwd())

        self.file_list = []
        # 方法回撥
        self.ftp.dir(self.get_file_list)

        remote_names = self.file_list
        self.debug_print('遠端目錄 列表: %s' % remote_names)
        for item in remote_names:
            file_type = item[0]
            file_name = item[1]
            local = os.path.join(local_path, file_name)
            if file_type == 'd':
                print("download_file_tree()---> 下載目錄： %s" % file_name)
                self.download_file_tree(local, file_name)
            elif file_type == '-':
                print("download_file()---> 下載檔案： %s" % file_name)
                self.download_file(local, file_name)
            self.ftp.cwd("..")
            self.debug_print('返回上層目錄 %s' % self.ftp.pwd())
        return True

    def upload_file(self, local_file, remote_file):
        """從本地上傳檔案到ftp

           引數:
             local_path: 本地檔案

             remote_path: 遠端檔案
        """
        if not os.path.isfile(local_file):
            self.debug_print('%s 不存在' % local_file)
            return

        if self.is_same_size(local_file, remote_file):
            self.debug_print('跳過相等的檔案: %s' % local_file)
            return

        buf_size = 1024
        file_handler = open(local_file, 'rb')
        self.ftp.storbinary('STOR %s' % remote_file, file_handler, buf_size)
        file_handler.close()
        self.debug_print('上傳: %s' % local_file + "成功!")

    def upload_file_tree(self, local_path, remote_path):
        """從本地上傳目錄下多個檔案到ftp
           引數:

             local_path: 本地路徑

             remote_path: 遠端路徑
        """
        if not os.path.isdir(local_path):
            self.debug_print('本地目錄 %s 不存在' % local_path)
            return

        self.ftp.cwd(remote_path)
        self.debug_print('切換至遠端目錄: %s' % self.ftp.pwd())

        local_name_list = os.listdir(local_path)
        for local_name in local_name_list:
            src = os.path.join(local_path, local_name)
            if os.path.isdir(src):
                try:
                    self.ftp.mkd(local_name)
                except Exception as err:
                    self.debug_print("目錄已存在 %s ,具體錯誤描述為：%s" % (local_name, err))
                self.debug_print("upload_file_tree()---> 上傳目錄： %s" % local_name)
                self.upload_file_tree(src, local_name)
            else:
                self.debug_print("upload_file_tree()---> 上傳檔案： %s" % local_name)
                self.upload_file(src, local_name)
        self.ftp.cwd("..")

    def close(self):
        """ 退出ftp
        """
        self.debug_print("close()---> FTP退出")
        self.ftp.quit()
        self.log_file.close()

    def debug_print(self, s):
        """ 列印日誌
        """
        self.write_log(s)

    def deal_error(self, e):
        """ 處理錯誤異常
            引數：
                e：異常
        """
        log_str = '發生錯誤: %s' % e
        self.write_log(log_str)
        sys.exit()

    def write_log(self, log_str):
        """ 記錄日誌
            引數：
                log_str：日誌
        """
        time_now = time.localtime()
        date_now = time.strftime('%Y-%m-%d', time_now)
        format_log_str = "%s ---> %s \n " % (date_now, log_str)
        print(format_log_str)
        self.log_file.write(format_log_str)

    def get_file_list(self, line):
        """ 獲取檔案列表
            引數：
                line：
        """
        file_arr = self.get_file_name(line)
        # 去除  . 和  ..
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)

    def get_file_name(self, line):
        """ 獲取檔名
            引數：
                line：
        """
        pos = line.rfind(':')
        while (line[pos] != ' '):
            pos += 1
        while (line[pos] == ' '):
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr


if __name__ == "__main__":
    my_ftp = MyFTP("192.168.50.51")
    my_ftp.login("pi", "123")

    # 下載單個檔案
    my_ftp.download_file("C:/Users/danie/Desktop", "/home/pi/socket_cam/result/test.txt")

    # 下載目錄
    # my_ftp.download_file_tree("G:/ftp_test/", "App/AutoUpload/ouyangpeng/I12/")

    # 上傳單個檔案
    # my_ftp.upload_file("G:/ftp_test/Release/XTCLauncher.apk", "/App/AutoUpload/ouyangpeng/I12/Release/XTCLauncher.apk")

    # 上傳目錄
    # my_ftp.upload_file_tree("G:/ftp_test/", "/App/AutoUpload/ouyangpeng/I12/")

    my_ftp.close()