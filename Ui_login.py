# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wangtong\Desktop\DL-GUI\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogin(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(393, 282)
        login.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(100, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(login)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(login)
        self.textBrowser.setGeometry(QtCore.QRect(90, 110, 221, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(login)
        self.textBrowser_2.setGeometry(QtCore.QRect(90, 50, 221, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(40, 52, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "login"))
        self.pushButton.setText(_translate("login", "登录"))
        self.pushButton_2.setText(_translate("login", "退出"))
        self.label.setText(_translate("login", "账户："))
        self.label_2.setText(_translate("login", "密码："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_dialogin()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

