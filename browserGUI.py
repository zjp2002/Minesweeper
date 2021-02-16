# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_browser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import configparser

class Ui_Form(object):
    def __init__(self, k):
        config = configparser.ConfigParser()
        config.read('gameSetting.ini')
        self.URL = config['BROWSER']['URL' + str(k)]
        self.gain = config.getfloat('BROWSER', 'gain' + str(k))

        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 800)
        Form.setMinimumSize(QtCore.QSize(1300, 800))
        Form.setMaximumSize(QtCore.QSize(1300, 800))
        Form.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/cat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.webEngineView = QWebEngineView(Form)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.webEngineView.setMinimumSize(QtCore.QSize(1300, 800))
        self.webEngineView.setMaximumSize(QtCore.QSize(1300, 800))
        self.webEngineView.setMouseTracking(False)
        self.webEngineView.setUrl(QtCore.QUrl(self.URL))
        self.webEngineView.setZoomFactor(self.gain)
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "黑猫浏览器"))


