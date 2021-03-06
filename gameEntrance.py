# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\unbelievable\PycharmProjects\pythonProject\ui_entrance.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import gameRank
import configparser
import os
import json

global flag
flag = False


class Ui_Form(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.Dialog.setWindowIcon(QtGui.QIcon("media/cat.ico"))
        config = configparser.ConfigParser()

        file = "scoreB.json"
        if  os.path.exists(file) :
            sz = os.path.getsize(file)
            if not sz:
                self.Flag=False
            else:
                self.Flag = True
        else:
            self.Flag = False

        if not self.Flag:
            list=[]
            with open('scoreB.json', mode='w', encoding='utf-8') as fp:
                json.dump(list, fp)

        file = "scoreC.json"
        if os.path.exists(file):
            sz = os.path.getsize(file)
            if not sz:
                self.Flag = False
            else:
                self.Flag = True
        else:
            self.Flag = False

        if not self.Flag:
            list = []
            with open('scoreC.json', mode='w', encoding='utf-8') as fp:
                json.dump(list, fp)

        file = "scoreE.json"
        if os.path.exists(file):
            sz = os.path.getsize(file)
            if not sz:
                self.Flag = False
            else:
                self.Flag = True
        else:
            self.Flag = False

        if not self.Flag:
            list = []
            with open('scoreE.json', mode='w', encoding='utf-8') as fp:
                json.dump(list, fp)

        file = "scoreI.json"
        if os.path.exists(file):
            sz = os.path.getsize(file)
            if not sz:
                self.Flag = False
            else:
                self.Flag = True
        else:
            self.Flag = False

        if not self.Flag:
            list = []
            with open('scoreI.json', mode='w', encoding='utf-8') as fp:
                json.dump(list, fp)

        if not config.read('gameSetting.ini'):
            self.min3BV = 2
            self.max3BV = 54
            self.timesLimit = 1000
            self.enuLimit = 30
            self.gameMode = 0
            self.transparency = 1
            self.pixSize = 30
            self.mainWinTop = 100
            self.mainWinLeft = 200
            self.row = 8
            self.column = 8
            self.mineNum = 10
            config["DEFAULT"] = {'timesLimit': 1000,
                                 'enuLimit': 30,
                                 'gameMode': 0,
                                 'transparency': 100,
                                 'pixSize': 30,
                                 'mainWinTop': 100,
                                 'mainWinLeft': 200,
                                 'gameDifficult': 'B'
                                 }
            config["BEGINNER"] = {'min3BV': 2,
                                  'max3BV': 54,
                                  }
            config["INTERMEDIATE"] = {'min3BV': 30,
                                      'max3BV': 216,
                                      }
            config["EXPERT"] = {'min3BV': 100,
                                'max3BV': 381,
                                }
            config["CUSTOM"] = {'x': 8,
                                'y': 8,
                                'n': 10,
                                'min3BV': 2,
                                'max3BV': 54,
                                }
            '''
            config["BROWSER"] = {'URL1':"http://saolei.wang/Main/Index.asp",
                                'URL2':"http://www.minesweeper.info/worldranking.html",
                                'URL3':"https://cn.bing.com/?mkt=zh-CN",
                                'gain1':1.0,
                                'gain2':1.0,
                                'gain3':1.0,
                                 }
            '''
            with open('gameSetting.ini', 'w') as configfile:
                config.write(configfile)  # 将对象写入文件

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(561, 572)
        Form.setFixedSize(561, 572)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("media/blue.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 0, 371, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("media/minesweeper.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(460, 0, 101, 571))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 150, 361, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_29.addWidget(self.pushButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem5)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(100, 250, 361, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_27.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(100, 350, 361, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem)
        self.pushButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(24)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_26.addWidget(self.pushButton_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem1)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(100, 450, 361, 71))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem6)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_30.addWidget(self.pushButton_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem7)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 101, 571))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")

        self.retranslateUi(Form)
        self.pushButton_1.clicked.connect(self.gao_ji)
        self.pushButton_1.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(self.zhong_ji)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton_3.clicked.connect(self.chu_ji)
        self.pushButton_3.clicked.connect(Form.close)
        self.pushButton_4.clicked.connect(self.openRank)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "扫雷"))
        self.pushButton_1.setText(_translate("Form", "    高级    "))
        self.pushButton_2.setText(_translate("Form", "    中级    "))
        self.pushButton_3.setText(_translate("Form", "    初级    "))
        self.pushButton_4.setText(_translate("Form", "   排行榜   "))

    def openRank(self):
        ui = gameRank.Ui_MainWindow()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()

    def gao_ji(self, Form):
        conf = configparser.ConfigParser()
        conf.read("gameSetting.ini")
        conf.set('DEFAULT', 'gamedifficult', 'E')
        conf.write(open('gameSetting.ini', 'r+', encoding="utf-8"))
        global flag
        flag = True

    def zhong_ji(self, Form):
        conf = configparser.ConfigParser()
        conf.read("gameSetting.ini")
        conf.set('DEFAULT', 'gamedifficult', 'I')
        conf.write(open('gameSetting.ini', 'r+', encoding="utf-8"))
        global flag
        flag = True

    def chu_ji(self, Form):
        conf = configparser.ConfigParser()
        conf.read("gameSetting.ini")
        conf.set('DEFAULT', 'gamedifficult', 'B')
        conf.write(open('gameSetting.ini', 'r+', encoding="utf-8"))
        global flag
        flag = True


def Flag():
    global flag
    return flag
