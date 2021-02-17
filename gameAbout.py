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
            self.Dialog.setWindowIcon (QtGui.QIcon ("media/cat.ico"))
            self.pushButton.clicked.connect (self.processParameter)

        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(600, 382)
            Form.setMinimumSize(QtCore.QSize(600, 382))
            Form.setMaximumSize(QtCore.QSize(600, 382))
            Form.setSizeIncrement(QtCore.QSize(0, 0))
            Form.setWindowOpacity(10.0)
            self.pushButton = QtWidgets.QPushButton(Form)
            self.pushButton.setGeometry(QtCore.QRect(150, 330, 281, 41))
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
            self.label_5 = QtWidgets.QLabel(Form)
            self.label_5.setGeometry(QtCore.QRect(40, 70, 541, 191))
            font = QtGui.QFont()
            font.setFamily("黑体")
            font.setPointSize(20)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(75)
            font.setStrikeOut(False)
            self.label_5.setFont(font)
            self.label_5.setTextFormat(QtCore.Qt.RichText)
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(Form)
            self.label_6.setGeometry(QtCore.QRect(50, 20, 51, 51))
            # self.label_6.setStyleSheet("border-image: url(media/github.svg);")
            self.label_6.setText("")
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(Form)
            self.label_7.setGeometry(QtCore.QRect(50, 90, 61, 61))
            self.label_7.setAutoFillBackground(False)
            # self.label_7.setStyleSheet("border-image: url(media/weixin.svg);")
            self.label_7.setText("")
            self.label_7.setObjectName("label_7")

            self.retranslateUi(Form)
            self.pushButton.clicked.connect(Form.close)
            QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "关于"))
            self.pushButton.setText(_translate("Form", "确定"))
            self.pushButton.setShortcut(_translate("Form", "Space"))
            self.label_5.setText(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'黑体\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
                                            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">①软件可以无限制复制、储存、传播。营销号转载请标明<br />本项目的github地址：<br />https://github.com/jayzjp/Minesweeper</span></p>\n"
                                            "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">②任何人可以在任何一个项目中使用本项目源代码的任何<br />一个部分。本项目为原作者黑猫扫雷的二次创作。</span></p></body></html>"))

        def processParameter(self):
            self.Dialog.close()





