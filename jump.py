from PyQt5 import QtCore, QtGui, QtWidgets
from Mainwindow import Mainwindow1
from login import dialogin
from picsized import picturesize as Pic

class Ui_login(dialogin):
    def __init__(self):
        super(dialogin, self).__init__()
        self.setupUi(self)

class Ui_PictureSize(Pic):
    def __init__(self):
        super(Pic, self).__init__()
        self.setupUi(self)

class Mainwindow1(Mainwindow1):
    def __init__(self):
        super(Mainwindow1, self).__init__()
        self.setupUi(self)
    
  #定义登录按钮的功能
    def loginEvent(self):
        self.hide()
        self.dia = Ui_login()
        self.dia.show()
    def Picturesize1(self):
        self.hide()
        self.dia = Ui_PictureSize
        self.dia.show()
        
    #运行窗口Login
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    main = Mainwindow1()
    login=Ui_login()
    Picsize = Ui_PictureSize()

    main.show()
    login.pushButton.clicked.connect(login.show)
    login.pushButton_2.clicked.connect(Picsize.show())
    sys.exit(app.exec_())









