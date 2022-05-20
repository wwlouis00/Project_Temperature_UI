from PyQt5 import QtCore,QtGui,QtWidgets
from FTP3 import Ui_MainWindow
import sys


class test(object):
    
    def test1(self):
        print("test1234")
    '''
    print('testtest')
    '''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())