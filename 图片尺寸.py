# -*- coding: utf-8 -*-

"""
Module implementing UI_图片尺寸.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_图片尺寸 import Ui_MainWindow


class UI_图片尺寸(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(UI_图片尺寸, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_action_3_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
