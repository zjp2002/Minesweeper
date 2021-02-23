from PyQt5 import QtCore, QtGui, QtWidgets
import configparser


class Ui_Form(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('gameSetting.ini')
        self.gameMode = config.getint('DEFAULT', 'gameMode')
        self.transparency = config.getint('DEFAULT', 'transparency')
        self.pixSize = config.getint('DEFAULT', 'pixSize')

        self.alter = False
        self.Dialog = QtWidgets.QDialog()
        self.setupUi(self.Dialog)
        self.setParameter()
        self.Dialog.setWindowIcon(QtGui.QIcon("media/cat.ico"))
        self.pushButton.clicked.connect(self.processParameter)
        self.pushButton_2.clicked.connect(self.Dialog.close)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(671, 423)
        Form.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/11762/.designer/backup/media/cat.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 50, 91, 51))
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 150, 91, 51))
        self.pushButton_2.setStyleSheet("border-image: url(media/button.png);\n"
                                        "font: 16pt \"黑体\";\n"
                                        "color:white;font: bold;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 50, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(490, -40, 16, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 220, 671, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 240, 621, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 0, 3, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 0, 2, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 1, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 40, 151, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(260, 150, 160, 22))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 140, 91, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(420, 140, 31, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setText("")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(460, 140, 21, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        self.horizontalSlider.valueChanged['int'].connect(self.label_7.setNum)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "游戏设置"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.radioButton.setText(_translate("Form", "标准"))
        self.radioButton_7.setText(_translate("Form", "强可猜"))
        self.radioButton_4.setText(_translate("Form", "弱无猜"))
        self.radioButton_5.setText(_translate("Form", "竞速无猜"))
        self.radioButton_8.setText(_translate("Form", "弱可猜"))
        self.radioButton_2.setText(_translate("Form", "Win7"))
        self.radioButton_3.setText(_translate("Form", "强无猜"))
        self.radioButton_6.setText(_translate("Form", "准无猜"))
        self.label_6.setText(_translate("Form", "方格边长"))
        self.label_5.setText(_translate("Form", "透明度"))
        self.label_8.setText(_translate("Form", "%"))

    def setParameter(self):
        self.lineEdit_5.setText(str(self.pixSize))
        self.horizontalSlider.setValue(self.transparency)
        self.label_7.setText(str(self.transparency))
        # gameMode = 0，1，2，3，4，5，6，7代表：
        # 标准、win7、竞速无猜、强无猜、弱无猜、准无猜、强可猜、弱可猜
        if self.gameMode == 0:
            self.radioButton.setChecked(True)
        elif self.gameMode == 1:
            self.radioButton_2.setChecked(True)
        elif self.gameMode == 2:
            self.radioButton_5.setChecked(True)
        elif self.gameMode == 3:
            self.radioButton_3.setChecked(True)
        elif self.gameMode == 4:
            self.radioButton_4.setChecked(True)
        elif self.gameMode == 5:
            self.radioButton_6.setChecked(True)
        elif self.gameMode == 6:
            self.radioButton_7.setChecked(True)
        else:
            self.radioButton_8.setChecked(True)

    def processParameter(self):
        # 只有点确定才能进来

        self.alter = True
        self.transparency = self.horizontalSlider.value()
        self.pixSize = int(self.lineEdit_5.text())
        # gameMode = 0，1，2，3，4，5，6，7代表：
        # 标准、win7、竞速无猜、强无猜、弱无猜、准无猜、强可猜、弱可猜
        if self.radioButton.isChecked() == True:
            self.gameMode = 0
        elif self.radioButton_2.isChecked() == True:
            self.gameMode = 1
        elif self.radioButton_3.isChecked() == True:
            self.gameMode = 3
        elif self.radioButton_4.isChecked() == True:
            self.gameMode = 4
        elif self.radioButton_5.isChecked() == True:
            self.gameMode = 2
        elif self.radioButton_6.isChecked() == True:
            self.gameMode = 5
        elif self.radioButton_7.isChecked() == True:
            self.gameMode = 6
        elif self.radioButton_8.isChecked() == True:
            self.gameMode = 7

        conf = configparser.ConfigParser()
        conf.read("gameSetting.ini")
        conf.set("DEFAULT", "gameMode", str(self.gameMode))
        conf.set("DEFAULT", "transparency", str(self.transparency))
        conf.set("DEFAULT", "pixSize", str(self.pixSize))
        conf.write(open('gameSetting.ini', "w"))

        self.Dialog.close()
