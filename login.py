# -*- coding: utf-8 -*-

"""
Module implementing login.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_login import Ui_login


class Dialogin(QDialog, Ui_login):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialogin, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(bool)
    def on_textEdit_copyAvailable(self, b):
        """
        Slot documentation goes here.
        
        @param b DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        raise NotImplementedError
