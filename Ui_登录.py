# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wangtong\Desktop\DL-GUI\登录.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(289, 207)
        login.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(login)
        self.pushButton.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(login)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 140, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(40, 40, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(login)
        self.textEdit.setGeometry(QtCore.QRect(90, 30, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(login)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 80, 141, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(login)
        self.pushButton_2.clicked.connect(login.close)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "登录"))
        self.pushButton.setText(_translate("login", "登录"))
        self.pushButton_2.setText(_translate("login", "退出"))
        self.label.setText(_translate("login", "账号："))
        self.label_2.setText(_translate("login", "密码："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

