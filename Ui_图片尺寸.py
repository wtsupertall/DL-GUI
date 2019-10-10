# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wangtong\Desktop\DL-GUI\图片尺寸.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PIcsize(object):
    def setupUi(self, PIcsize):
        PIcsize.setObjectName("PIcsize")
        PIcsize.resize(791, 605)
        self.centralWidget = QtWidgets.QWidget(PIcsize)
        self.centralWidget.setObjectName("centralWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 181, 581))
        self.textBrowser.setObjectName("textBrowser")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(180, 40, 611, 541))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 0, 611, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_2 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 0, 1, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 0, 2, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 0, 3, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout.addWidget(self.toolButton_5, 0, 4, 1, 1)
        PIcsize.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(PIcsize)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 791, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        PIcsize.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(PIcsize)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(PIcsize)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(PIcsize)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(PIcsize)
        QtCore.QMetaObject.connectSlotsByName(PIcsize)

    def retranslateUi(self, PIcsize):
        _translate = QtCore.QCoreApplication.translate
        PIcsize.setWindowTitle(_translate("PIcsize", "MainWindow"))
        self.toolButton_2.setText(_translate("PIcsize", "工具2"))
        self.toolButton.setText(_translate("PIcsize", "工具1"))
        self.toolButton_3.setText(_translate("PIcsize", "工具3"))
        self.toolButton_4.setText(_translate("PIcsize", "工具4"))
        self.toolButton_5.setText(_translate("PIcsize", "工具5"))
        self.menu.setTitle(_translate("PIcsize", "文件"))
        self.action.setText(_translate("PIcsize", "保存"))
        self.action_2.setText(_translate("PIcsize", "退出"))
        self.action_3.setText(_translate("PIcsize", "打开"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PIcsize = QtWidgets.QMainWindow()
    ui = Ui_PIcsize()
    ui.setupUi(PIcsize)
    PIcsize.show()
    sys.exit(app.exec_())

