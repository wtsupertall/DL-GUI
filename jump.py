from PyQt5 import  QtWidgets
from login import dialoglogin
from camera1 import Dialogca
from camera2 import Dialogca2
from mainframe import MainWindow
from jiemian import MainWindow1
from connect import Dialogcon
from trans import Dialogtrans
from save import dialogsave
class dialoglogin(dialoglogin):
    def __init__(self):
        super(dialoglogin,self).__init__()
        self.setupUi(self)
        
class Dialogca(Dialogca):
    def __init__(self):
        super(Dialogca,self).__init__()
        self.setupUi(self)
        
class Dialogca2(Dialogca2):
    def __init__(self):
        super(Dialogca2,self).__init__()
        self.setupUi(self)
        
class Dialogcon(Dialogcon):
     def __init__(self):
        super(Dialogcon,self).__init__()
        self.setupUi(self)
        
class Dialogtrans(Dialogtrans):
     def __init__(self):
        super(Dialogtrans,self).__init__()
        self.setupUi(self)

class jiemian(MainWindow1):
    def __init__(self):
        super(MainWindow1,self).__init__()
        self.setupUi(self)   

class MainWindow(MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

class dialogsave(dialogsave):
     def __init__(self):
        super(dialogsave,self).__init__()
        self.setupUi(self)   

def loginEvent(self):
        self.hide()
        self.dia = dialoglogin()
        self.dia.show()
        
        self.hide()
        self.dia1 = MainWindow1()
        self.dia1.show()
        
        self.hide()
        self.dia2 = Dialogca()
        self.dia2.show()
        
        self.hide()
        self.dia4 = Dialogca2()
        self.dia4.show()  
        
        self.hide()
        self.dia3 = Dialogcon()
        self.dia3.show()  
        
        self.hide()
        self.dia5 = Dialogtrans()
        self.dia5.show()
        
        self.hide()
        self.dia6 = dialogsave()
        self.dia6.show()

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    login=MainWindow()
    dial = dialoglogin()
    caculate = MainWindow1()
    camera1 = Dialogca()
    camera2 = Dialogca2()
    connect1 = Dialogcon()
    coordtrans = Dialogtrans()
    save =  dialogsave()
    login.show()
    login.action_3.triggered.connect(dial.show)
    login.actionECEF.triggered.connect(caculate.show)
    login.action_15.triggered.connect(camera1.show)
    login.action_17.triggered.connect(camera2.show)
    login.action_18.triggered.connect(connect1.show)
    login.action_4.triggered.connect(coordtrans.show)
    login.action_5.triggered.connect(save.show)
    sys.exit(app.exec_())









