# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scores.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import gameRank

class Ui_Form(object):
    def __init__(self, scores):
        self.scores = scores
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(503, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(503, 450))
        Form.setMaximumSize(QtCore.QSize(503, 450))
        Form.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("media/cat.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setToolTip("")
        Form.setToolTipDuration(-1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(160, 110, 261, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setLineWidth(4)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setItem(2, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(136)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(48)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 271, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("\n"
                                   "font: 18pt \"幼圆\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 461, 181))
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5.setLineWidth(4)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 461, 52))
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setLineWidth(7)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 290, 461, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 359, 461, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.saveScores)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "成绩"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Difficulty"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Time"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3BV/s"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "游戏难度："))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", self.scores['Difficulty']))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "游戏用时："))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", self.scores['Time']))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "3BV/s："))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", self.scores['3BV/s']))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", ">>>您的游戏成绩<<<"))
        self.lineEdit.setPlaceholderText(_translate("Form", "请输入玩家姓名"))
        self.pushButton.setText(_translate("Form", "保存"))
        self.pushButton_2.setText(_translate("Form", "放弃"))

    def saveScores(self):
        if self.scores['Difficulty'] == '初级':
            self.saveScoreB()
            flag = 0
        elif self.scores['Difficulty'] == '中级':
            self.saveScoreI()
            flag = 1
        elif self.scores['Difficulty'] == '高级':
            self.saveScoreE()
            flag = 2
        elif self.scores['Difficulty'] == '自定义':
            self.saveScoreC()
            flag = 3
        self.Dialog.close()
        self.action_QEvent(flag)

    def saveScoreB(self):
        '''
        temp_dict = {}
        with open('scoreB.json', mode='r', encoding='utf-8') as fp:
            data = json.load(fp)
        with open('scoreB.json', mode='w', encoding='utf-8') as fp:
            temp_dict['name'] = self.lineEdit.text()
            temp_dict['Time'] = self.scores['Time']
            temp_dict['3BV/s'] = self.scores['3BV/s']
            data.append(temp_dict)
            json.dump(data, fp)

        '''
        temp_dict = {}
        if self.lineEdit.text():
            temp_dict['name'] = self.lineEdit.text()
        else:
            temp_dict['name'] = "(^_^)"
        temp_dict['time'] = self.scores['Time']
        temp_dict['3bv/s'] = self.scores['3BV/s']
        list=[]
        with open('scoreB.json', mode='r', encoding='utf-8') as fp:
            list = json.load(fp)
        if list == []:
            list.append(temp_dict)
        else:
            flag = 0
            flag1 = True
            for data in list:
                if temp_dict['time'] >= data['time']:
                    flag += 1
                else:
                    list.insert(flag, temp_dict)
                    flag1 = False
                    break
            if flag1 and flag <= 9:
                list.append(temp_dict)
        while len(list) > 10:
            list.pop()
        with open('scoreB.json', mode='w', encoding='utf-8') as fp:
            json.dump(list, fp)


    def saveScoreI(self):
        temp_dict = {}
        if self.lineEdit.text():
            temp_dict['name'] = self.lineEdit.text()
        else:
            temp_dict['name'] = "(^_^)"
        temp_dict['time'] = self.scores['Time']
        temp_dict['3bv/s'] = self.scores['3BV/s']
        list = []
        with open('scoreI.json', mode='r', encoding='utf-8') as fp:
            list = json.load(fp)
        if list == []:
            list.append(temp_dict)
        else:
            flag = 0
            flag1 = True
            for data in list:
                if temp_dict['time'] >= data['time']:
                    flag += 1
                else:
                    list.insert(flag, temp_dict)
                    flag1 = False
                    break
            if flag1 and flag <= 9:
                list.append(temp_dict)
        while len(list) > 10:
            list.pop()
        with open('scoreI.json', mode='w', encoding='utf-8') as fp:
            json.dump(list, fp)

    def saveScoreE(self):
        temp_dict = {}
        if self.lineEdit.text():
            temp_dict['name'] = self.lineEdit.text()
        else:
            temp_dict['name'] = "(^_^)"
        temp_dict['time'] = self.scores['Time']
        temp_dict['3bv/s'] = self.scores['3BV/s']
        list = []
        with open('scoreE.json', mode='r', encoding='utf-8') as fp:
            list = json.load(fp)
        if list == []:
            list.append(temp_dict)
        else:
            flag = 0
            flag1 = True
            for data in list:
                if temp_dict['time'] >= data['time']:
                    flag += 1
                else:
                    list.insert(flag, temp_dict)
                    flag1 = False
                    break
            if flag1 and flag <= 9:
                list.append(temp_dict)
        while len(list) > 10:
            list.pop()
        with open('scoreE.json', mode='w', encoding='utf-8') as fp:
            json.dump(list, fp)

    def saveScoreC(self):
        temp_dict = {}
        if self.lineEdit.text():
            temp_dict['name'] = self.lineEdit.text()
        else:
            temp_dict['name'] = "(^_^)"
        temp_dict['time'] = self.scores['Time']
        temp_dict['3bv/s'] = self.scores['3BV/s']
        list = []
        with open('scoreC.json', mode='r', encoding='utf-8') as fp:
            list = json.load(fp)
        if list == []:
            list.append(temp_dict)
        else:
            flag = 0
            flag1 = True
            for data in list:
                if temp_dict['3bv/s'] <= data['3bv/s']:
                    flag += 1
                else:
                    list.insert(flag, temp_dict)
                    flag1 = False
                    break
            if flag1 and flag <= 9:
                list.append(temp_dict)
        while len(list) > 10:
            list.pop()
        with open('scoreC.json', mode='w', encoding='utf-8') as fp:
            json.dump(list, fp)

    def action_QEvent(self, flag):
        # 本地战绩
        ui = gameRank.Ui_MainWindow()
        ui.tabWidget.setCurrentIndex(flag)
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()
