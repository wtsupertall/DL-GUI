from PyQt5 import QtCore, QtGui, QtWidgets

from login import Dialogin


class Ui_login(QtWidgets.QDialog,Dialogin):
    def __init__(self):
        super(Ui_similarty,self).__init__()
        self.setupUi(self)


class Ui_similarty(QtWidgets.QDialog,Ui_Dialog2):
    def __init__(self):
        super(Ui_similarty,self).__init__()
        self.setupUi(self)

class Ui_file(QtWidgets.QDialog,Ui_check_file):
    def __init__(self):
        super(Ui_file,self).__init__()
        self.setupUi(self)


class Ui_Dialog(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)

    def checkfile(self):
        self.hide()
        self.c = Ui_file()
        self.c.show()
        
    #定义登录按钮的功能
    def loginEvent(self):
        self.hide()
        self.dia = Ui_Dialog()
        self.dia.show()
        
    def loginEvent2(self):
        self.hide()
        self.dia = Ui_login()
        self.dia.show()    
        
    #运行窗口Login
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    login=loginWindow()
    dial = Ui_Dialog()
    file = Ui_file()
    simi = Ui_similarty()
    login.show()
    login.pushButton.clicked.connect(dial.show)
    dial.pushButton.clicked.connect(file.show)
    dial.pushButton_2.clicked.connect(simi.show)
    sys.exit(app.exec_())









