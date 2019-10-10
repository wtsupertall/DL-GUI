# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wangtong\Desktop\DL-GUI\图片裁剪.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PictureSize(object):
    def setupUi(self, PictureSize):
        PictureSize.setObjectName("PictureSize")
        PictureSize.resize(703, 600)
        self.centralWidget = QtWidgets.QWidget(PictureSize)
        self.centralWidget.setObjectName("centralWidget")
        PictureSize.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(PictureSize)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 703, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setObjectName("menu_5")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        PictureSize.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(PictureSize)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(PictureSize)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(PictureSize)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(PictureSize)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(PictureSize)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(PictureSize)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(PictureSize)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(PictureSize)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(PictureSize)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(PictureSize)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(PictureSize)
        self.action_11.setObjectName("action_11")
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menu_4.addAction(self.action_10)
        self.menu_4.addAction(self.action_11)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_9)
        self.menu.addAction(self.action_5)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())

        self.retranslateUi(PictureSize)
        QtCore.QMetaObject.connectSlotsByName(PictureSize)

    def retranslateUi(self, PictureSize):
        _translate = QtCore.QCoreApplication.translate
        PictureSize.setWindowTitle(_translate("PictureSize", "MainWindow"))
        self.menu_2.setTitle(_translate("PictureSize", "裁剪"))
        self.menu_4.setTitle(_translate("PictureSize", "帮助"))
        self.menu_5.setTitle(_translate("PictureSize", "设置"))
        self.menu.setTitle(_translate("PictureSize", "文件"))
        self.action.setText(_translate("PictureSize", "打开图片"))
        self.action_2.setText(_translate("PictureSize", "打开文件夹"))
        self.action_3.setText(_translate("PictureSize", "保存"))
        self.action_4.setText(_translate("PictureSize", "关闭"))
        self.action_5.setText(_translate("PictureSize", "退出"))
        self.action_6.setText(_translate("PictureSize", "任选区域裁剪"))
        self.action_7.setText(_translate("PictureSize", "指定裁剪框大小"))
        self.action_8.setText(_translate("PictureSize", "裁剪结果预览"))
        self.action_9.setText(_translate("PictureSize", "另存为"))
        self.action_10.setText(_translate("PictureSize", "帮助文档"))
        self.action_11.setText(_translate("PictureSize", "关于"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PictureSize = QtWidgets.QMainWindow()
    ui = Ui_PictureSize()
    ui.setupUi(PictureSize)
    PictureSize.show()
    sys.exit(app.exec_())

