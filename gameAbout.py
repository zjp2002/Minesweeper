# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.Dialog.setWindowIcon(QtGui.QIcon("media/cat.ico"))
        self.pushButton.clicked.connect(self.processParameter)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 600)
        Form.setFixedSize(450, 600)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(85, 530, 280, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("border-image: url(media/button.png);\n"
"font: 16pt \"黑体\";\n"
"color:white;font: bold;")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(171, 20, 128, 128))
        self.icon.setStyleSheet("border-image: url(media/cat.ico);")
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 45, 45))
        self.label_2.setStyleSheet("border-image: url(media/github.svg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 220, 301, 71))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(175, 150, 100, 30))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(35, 320, 390, 190))
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton.setShortcut(_translate("Form", "Space"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><a href=\"https://github.com/zjp2002/Minesweeper\"><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">https://github.com/zjp2002/<br/>Minesweeper</span></a></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#A9A9A9;\">科中扫雷</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt; font-weight:600;\">①本项目托管在Github上，可以点击上方<br/>链接联系我们</span></p><p align=\"justify\"><span style=\" font-size:12pt; font-weight:600;\">②本项目基于eee555的黑猫扫雷二次开发<br/>黑猫扫雷Github地址：<br/><a href=\"https://github.com/eee555/Solvable-Minesweeper\">https://github.com/eee555/Solvable-<br/>Minesweeper</span></a></p></body></html>"))

    def processParameter(self):
        self.Dialog.close()
