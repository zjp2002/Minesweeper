#内容已经全部注释，可以移除文件

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gs_more.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import configparser

'''
class Ui_Form(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('gameSetting.ini')
        self.URL1 = config['BROWSER']['URL1']
        self.URL2 = config['BROWSER']['URL2']
        self.URL3 = config['BROWSER']['URL3']
        self.gain1 = config.getfloat('BROWSER','gain1')
        self.gain2 = config.getfloat('BROWSER','gain2')
        self.gain3 = config.getfloat('BROWSER','gain3')

        self.alter = False
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)

        self.pushButton.clicked.connect (self.processParameter)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(461, 463)
        Form.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/cat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 50, 311, 81))
        self.plainTextEdit.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit.setLineWidth(3)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(350, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMinimum(0.2)
        self.doubleSpinBox.setMaximum(5.0)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setProperty("value", self.gain1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 410, 181, 41))
        self.pushButton_2.setStyleSheet("border-image: url(media/button.png);\n"
"font: 16pt \"黑体\";\n"
"color:white;font: bold;")
        self.pushButton_2.setShortcut("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setStyleSheet("border-image: url(media/button.png);\n"
"font: 16pt \"黑体\";\n"
"color:white;font: bold;")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 161, 31))
        self.label_3.setStyleSheet("font: 12pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(360, 20, 61, 31))
        self.label_4.setStyleSheet("font: 12pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(350, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.doubleSpinBox_2.setDecimals(2)
        self.doubleSpinBox_2.setMinimum(0.2)
        self.doubleSpinBox_2.setMaximum(5.0)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setProperty("value", self.gain2)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(360, 150, 61, 31))
        self.label_8.setStyleSheet("font: 12pt \"宋体\";")
        self.label_8.setObjectName("label_8")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(30, 180, 311, 81))
        self.plainTextEdit_2.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.plainTextEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEdit_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit_2.setLineWidth(3)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(350, 310, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.doubleSpinBox_3.setDecimals(2)
        self.doubleSpinBox_3.setMinimum(0.2)
        self.doubleSpinBox_3.setMaximum(5.0)
        self.doubleSpinBox_3.setSingleStep(0.01)
        self.doubleSpinBox_3.setProperty("value", self.gain3)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(360, 280, 61, 31))
        self.label_12.setStyleSheet("font: 12pt \"宋体\";")
        self.label_12.setObjectName("label_12")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(30, 310, 311, 81))
        self.plainTextEdit_3.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.plainTextEdit_3.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEdit_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit_3.setLineWidth(3)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 150, 161, 31))
        self.label_7.setStyleSheet("font: 12pt \"宋体\";")
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 280, 161, 31))
        self.label_11.setStyleSheet("font: 12pt \"宋体\";")
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "浏览器设置"))
        self.plainTextEdit.setPlainText(_translate("Form", self.URL1))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.label_3.setText(_translate("Form", "快捷键【5】，URL："))
        self.label_4.setText(_translate("Form", "放大："))
        self.label_8.setText(_translate("Form", "放大："))
        self.plainTextEdit_2.setPlainText(_translate("Form", self.URL2))
        self.label_12.setText(_translate("Form", "放大："))
        self.plainTextEdit_3.setPlainText(_translate("Form", self.URL3))
        self.label_7.setText(_translate("Form", "快捷键【6】，URL："))
        self.label_11.setText(_translate("Form", "快捷键【7】，URL："))

    def processParameter(self):
        #只有点确定才能进来
        
        self.alter = True
        self.URL1 = self.plainTextEdit.toPlainText()
        self.URL2 = self.plainTextEdit_2.toPlainText()
        self.URL3 = self.plainTextEdit_3.toPlainText()
        self.gain1 = self.doubleSpinBox.value()
        self.gain2 = self.doubleSpinBox_2.value()
        self.gain3 = self.doubleSpinBox_3.value()

        conf = configparser.ConfigParser()
        conf.read("gameSetting.ini")
        conf.set("BROWSER", "URL1", self.URL1)
        conf.set("BROWSER", "URL2", self.URL2)
        conf.set("BROWSER", "URL3", self.URL3)
        conf.set("BROWSER", "gain1", str(self.gain1))
        conf.set("BROWSER", "gain2", str(self.gain2))
        conf.set("BROWSER", "gain3", str(self.gain3))
        conf.write(open('gameSetting.ini', "w"))

        self.Dialog.close ()

'''