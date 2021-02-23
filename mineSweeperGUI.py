from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QCoreApplication
from PyQt5.QtGui import QPalette, QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QLineEdit, QInputDialog, QShortcut
import superGUI, mineLabel, selfDefinedParameter, gameSettings, gameHelp
import gameRank, gameAbout, gameTerms, browserGUI, gameScores
#import gameSetMoreGUI, gameAbout, gameTerms, browserGUI, gameScores
import random, sip
import minesweeper_master
import statusLabel
import configparser
import time


class MineSweeperGUI(superGUI.Ui_MainWindow):
    def __init__(self, MainWindow):
        config = configparser.ConfigParser()
        # gameMode = 0，1，2，3，4，5，6，7代表：
        # 标准、win7、竞速无猜、强无猜、弱无猜、准无猜、强可猜、弱可猜
        if config.read('gameSetting.ini'):
            # self.min3BV = config.getint('DEFAULT', 'min3BV')
            # self.max3BV = config.getint('DEFAULT', 'max3BV')
            self.timesLimit = config.getint('DEFAULT', 'timesLimit')
            self.enuLimit = config.getint('DEFAULT', 'enuLimit')
            self.gameMode = config.getint('DEFAULT', 'gameMode')
            self.transparency = (config.getint('DEFAULT', 'transparency') + 1) / 100
            self.pixSize = config.getint('DEFAULT', 'pixSize')
            self.mainWinTop = config.getint('DEFAULT', 'mainWinTop')
            self.mainWinLeft = config.getint('DEFAULT', 'mainWinLeft')
            if config['DEFAULT']['gameDifficult'] == 'B':
                self.row = 8
                self.column = 8
                self.mineNum = 10
                self.min3BV = config.getint('BEGINNER', 'min3BV')
                self.max3BV = config.getint('BEGINNER', 'max3BV')
            elif config['DEFAULT']['gameDifficult'] == 'I':
                self.row = 16
                self.column = 16
                self.mineNum = 40
                self.min3BV = config.getint('INTERMEDIATE', 'min3BV')
                self.max3BV = config.getint('INTERMEDIATE', 'max3BV')
            elif config['DEFAULT']['gameDifficult'] == 'E':
                self.row = 16
                self.column = 30
                self.mineNum = 99
                self.min3BV = config.getint('EXPERT', 'min3BV')
                self.max3BV = config.getint('EXPERT', 'max3BV')
            elif config['DEFAULT']['gameDifficult'] == 'C':
                self.row = config.getint('CUSTOM', 'x')
                self.column = config.getint('CUSTOM', 'y')
                self.mineNum = config.getint('CUSTOM', 'n')
                self.min3BV = config.getint('CUSTOM', 'min3BV')
                self.max3BV = config.getint('CUSTOM', 'max3BV')
        else:
            # 找不到配置文件就初始化
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
            config["CUSTOM"] = {'x':8,
                                'y':8,
                                'n':10,
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

        self.finish = False
        self.gamestart = False
        self.mainWindow = MainWindow
        self.mainWindow.setWindowIcon(QIcon("media/cat.ico"))
        self.mainWindow.setWindowOpacity(self.transparency)
        self.mainWindow.setFixedSize(self.mainWindow.minimumSize())
        self.mainWindow.move(self.mainWinTop, self.mainWinLeft)

        self.setupUi(self.mainWindow)
        self.mineLabel = []  # 局面
        self.operationStream = []
        self.gameWinFlag = False
        self.leftHeld = False
        self.leftAndRightHeld = False  # 鼠标是否被按下的标志位
        self.oldCell = (0, 0)  # 鼠标的上个停留位置，用于绘制按下去时的阴影
        self.boardofGame = [[10] * self.column for _ in range(self.row)]
        # boardofGame保存了判雷AI所看到的局面,不需要维护，只需要维持传递
        # 包括0~8，10代表未打开，11代表标雷
        # 比如，玩家没有标出来的雷，AI会在这上面标出来，但不一定标全
        self.notMine = []  # 保存AI判出来的雷

        self.matrixA = []
        self.matrixx = []
        self.matrixb = []
        self.enuLimitAI = 30  # AI采用的最大枚举长度限制
        self.board = [[0] * self.column for _ in range(self.row)]

        self.pixmapNum, self.pixmapLEDNum = self.importPic(self.pixSize) # 导入图片
        
        self.initMineArea()
        self.label_2.leftRelease.connect(self.gameRestart)
        # self.label_2.left
        self.label_2.setPixmap(self.pixmapNum[14])
        self.label_2.setScaledContents(True)
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.black)  # 设置字体颜色
        self.label_31.setPalette(pe)
        self.label_31.setFont(QFont("Arial", 20, QFont.Bold))
        self.label_32.setPalette(pe)
        self.label_32.setFont(QFont("Arial", 20, QFont.Bold))
        self.label_33.setPalette(pe)
        self.label_33.setFont(QFont("Arial", 20, QFont.Bold))
        self.label_11.setPalette(pe)
        self.label_11.setFont(QFont("Arial", 12, QFont.Bold))
        self.label_12.setPalette(pe)
        self.label_12.setFont(QFont("Arial", 12, QFont.Bold))
        self.label_13.setPalette(pe)
        self.label_13.setFont(QFont("Arial", 12, QFont.Bold))
        self.label_info.setPalette(pe)         # 最下面的框
        self.label_info.setFont(QFont("宋体", 12))
        #self.label_info.setText(str(self.mineNum))
        self.time = 0
        self.showTime(self.time)
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 一千秒回调一次的定时器
        self.timer.timeout.connect(self.timeCount)
        self.timeStart = False
        text4 = "按F2键或点击笑脸重新开始"
        self.label_info.setText(text4)
        self.mineUnFlagedNum = self.mineNum  # 没有标出的雷，显示在左上角
        self.showMineNum(self.mineUnFlagedNum)    # 在左上角画雷数

        # 绑定菜单栏事件
        self.actionnew_game.triggered.connect(self.gameRestart)
        self.actionchu_ji.triggered.connect(self.action_BEvent)
        self.actionzhogn_ji.triggered.connect(self.action_IEvent)
        self.actiongao_ji.triggered.connect(self.action_Event)
        self.actionzi_ding_yi.triggered.connect(self.action_CEvent)
        self.actiontui_chu.triggered.connect(QCoreApplication.instance().quit)
        self.actionyouxi_she_zhi.triggered.connect(self.action_NEvent)
        self.actionbdzj.triggered.connect(self.action_QEvent)
        #self.actionqita_she_zhi.triggered.connect(self.action_QEvent)
        self.actionxis.triggered.connect(self.action_HEvent)
        self.actiongaun_yv.triggered.connect(self.action_AEvent)
        self.actionrumjc.triggered.connect(self.action_JEvent)
        
        config = configparser.ConfigParser()
        config.read('gameSetting.ini')
        if config['DEFAULT']['gameDifficult'] == 'B':
            self.actionChecked('B')
        elif config['DEFAULT']['gameDifficult'] == 'I':
            self.actionChecked('I')
        elif config['DEFAULT']['gameDifficult'] == 'E':
            self.actionChecked('E')
        else:
            self.actionChecked('C')

        self.frameShortcut1.activated.connect(self.action_BEvent)
        self.frameShortcut2.activated.connect(self.action_IEvent)
        self.frameShortcut3.activated.connect(self.action_Event)
        self.frameShortcut4.activated.connect(self.gameRestart)
        #self.frameShortcut5.activated.connect(lambda: self.openBrowser(1))
        #self.frameShortcut6.activated.connect(lambda: self.openBrowser(2))
        #self.frameShortcut7.activated.connect(lambda: self.openBrowser(3))
        #self.frameShortcut8.activated.connect(self.showScores)

    def importPic(self, pixSize):
        # 导入资源，并缩放到希望的尺寸、比例
        pixmap0 = QPixmap("media/10.png")
        pixmap1 = QPixmap("media/11.png")
        pixmap2 = QPixmap("media/12.png")
        pixmap3 = QPixmap("media/13.png")
        pixmap4 = QPixmap("media/14.png")
        pixmap5 = QPixmap("media/15.png")
        pixmap6 = QPixmap("media/16.png")
        pixmap7 = QPixmap("media/17.png")
        pixmap8 = QPixmap("media/18.png")
        pixmap9 = QPixmap("media/00.png")
        pixmap10 = QPixmap("media/03.png")
        pixmap11 = QPixmap("media/02.png")
        pixmap12 = QPixmap("media/01.png")
        pixmap13 = QPixmap("media/04.png")
        pixmap14 = QPixmap("media/f0.png")
        pixmap15 = QPixmap("media/f1.png")
        pixmap16 = QPixmap("media/f2.png")
        pixmap17 = QPixmap("media/f3.png")
        pixmap18 = QPixmap("media/f4.png")
        pixmap0 = pixmap0.scaled(self.pixSize, self.pixSize)
        pixmap1 = pixmap1.scaled(self.pixSize, self.pixSize)
        pixmap2 = pixmap2.scaled(self.pixSize, self.pixSize)
        pixmap3 = pixmap3.scaled(self.pixSize, self.pixSize)
        pixmap4 = pixmap4.scaled(self.pixSize, self.pixSize)
        pixmap5 = pixmap5.scaled(self.pixSize, self.pixSize)
        pixmap6 = pixmap6.scaled(self.pixSize, self.pixSize)
        pixmap7 = pixmap7.scaled(self.pixSize, self.pixSize)
        pixmap8 = pixmap8.scaled(self.pixSize, self.pixSize)
        pixmap9 = pixmap9.scaled(self.pixSize, self.pixSize)
        pixmap10 = pixmap10.scaled(self.pixSize, self.pixSize)
        pixmap11 = pixmap11.scaled(self.pixSize, self.pixSize)
        pixmap12 = pixmap12.scaled(self.pixSize, self.pixSize)
        pixmap13 = pixmap13.scaled(self.pixSize, self.pixSize)
        pixmap14 = pixmap14.scaled(self.pixSize * 1.5, self.pixSize * 1.5)
        pixmap15 = pixmap15.scaled(self.pixSize * 1.5, self.pixSize * 1.5)
        pixmap16 = pixmap16.scaled(self.pixSize * 1.5, self.pixSize * 1.5)
        pixmap17 = pixmap17.scaled(self.pixSize * 1.5, self.pixSize * 1.5)
        pixmap18 = pixmap18.scaled(self.pixSize * 1.5, self.pixSize * 1.5)
        pixmapNum = {0: pixmap0, 1: pixmap1, 2: pixmap2, 3: pixmap3, 4: pixmap4,
                     5: pixmap5, 6: pixmap6, 7: pixmap7, 8: pixmap8, 9: pixmap9,
                     10: pixmap10, 11: pixmap11, 12: pixmap12, 13: pixmap13,
                     14: pixmap14, 15: pixmap15, 16: pixmap16, 17: pixmap17, 18: pixmap18}
        # 以上是读取数字的图片，局面中的数字；一下是上方LED数字的图片
        pixLEDmap0 = QPixmap("media/LED0.png")
        pixLEDmap1 = QPixmap("media/LED1.png")
        pixLEDmap2 = QPixmap("media/LED2.png")
        pixLEDmap3 = QPixmap("media/LED3.png")
        pixLEDmap4 = QPixmap("media/LED4.png")
        pixLEDmap5 = QPixmap("media/LED5.png")
        pixLEDmap6 = QPixmap("media/LED6.png")
        pixLEDmap7 = QPixmap("media/LED7.png")
        pixLEDmap8 = QPixmap("media/LED8.png")
        pixLEDmap9 = QPixmap("media/LED9.png")
        pixLEDmap0 = pixLEDmap0.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap1 = pixLEDmap1.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap2 = pixLEDmap2.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap3 = pixLEDmap3.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap4 = pixLEDmap4.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap5 = pixLEDmap5.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap6 = pixLEDmap6.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap7 = pixLEDmap7.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap8 = pixLEDmap8.scaled(self.pixSize, self.pixSize * 1.75)
        pixLEDmap9 = pixLEDmap9.scaled(self.pixSize, self.pixSize * 1.75)
        pixmapLEDNum = {0: pixLEDmap0, 1: pixLEDmap1, 2: pixLEDmap2, 3: pixLEDmap3,
                        4: pixLEDmap4, 5: pixLEDmap5, 6: pixLEDmap6, 7: pixLEDmap7,
                        8: pixLEDmap8, 9: pixLEDmap9}
        return pixmapNum, pixmapLEDNum

    def outOfBorder(self, i, j):
        if i < 0 or i >= self.row or j < 0 or j >= self.column:
            return True
        return False

    def layMine(self, i, j):  # mineLabel[r][c].num是真实局面，-1为雷，数字为数字
        xx = self.row
        yy = self.column
        num = self.mineNum
        if self.gameMode >= 3:  # 如果是模式3及以后，需要用判雷器
            self.boardofGame = [[10] * self.column for _ in range(self.row)]

        if self.gameMode == 2 or self.gameMode == 3 or self.gameMode == 6:
            # 根据模式生成局面
            Board, Parameters = minesweeper_master.layMineSolvable(xx, yy, num, i, j, self.min3BV, self.max3BV,
                                                                   self.timesLimit, self.enuLimit)
        elif self.gameMode == 0 or self.gameMode == 4 or self.gameMode == 5 or self.gameMode == 7:
            Board, Parameters = minesweeper_master.layMine(xx, yy, num, i, j, self.min3BV, self.max3BV, self.timesLimit)
        elif self.gameMode == 1:
            Board, Parameters = minesweeper_master.layMineOp(xx, yy, num, i, j, self.min3BV, self.max3BV,
                                                             self.timesLimit)
        '''
        if Parameters[0]:
            # text4 = 'Sucess! 3BV=%d\n尝试次数为%d'%(Parameters[1],Parameters[2])
            # text4 = 'ttt'
            text4 = 'Sucess! 尝试次数为%d'%(Parameters[2])
            self.label_info.setText(text4)
        else:
            # text4 = 'Failure! 3BV=%d\n尝试次数为%d'%(Parameters[1],Parameters[2])
            # text4 = 'iii'
            text4 = 'Failure! 尝试次数为%d' % (Parameters[2])
            self.label_info.setText(text4)
        '''

        for r in range(0, xx):
            for c in range(0, yy):
                self.mineLabel[r][c].num = Board[r][c]
                self.board[r][c] = Board[r][c]

    def initMineArea(self):
        self.gridLayout.setSpacing(0)  # 网格布局间距为0
        for i in range(0, self.row):
            self.mineLabel.append([])
            for j in range(0, self.column):
                label = mineLabel.mineLabel(i, j, 0, self.pixSize, "")
                label.setPixmap(self.pixmapNum[9])
                label.setMinimumSize(self.pixSize, self.pixSize)  # 改局面中的方格大小
                label.setAlignment(Qt.AlignCenter)

                # 绑定雷区点击事件
                label.leftPressed.connect(self.mineAreaLeftPressed)
                label.leftAndRightPressed.connect(self.mineAreaLeftAndRightPressed)
                label.leftAndRightRelease.connect(self.mineAreaLeftAndRightRelease)
                label.leftRelease.connect(self.mineAreaLeftRelease)
                label.rightPressed.connect(self.mineAreaRightPressed)
                label.rightRelease.connect(self.mineAreaRightRelease)

                label.mouseMove.connect(self.mineMouseMove)

                self.mineLabel[i].append(label)
                self.gridLayout.addWidget(label, i, j)  # 把子控件添加到网格布局管理器中

    def timeCount(self):  # 定时器改时间
        self.time += 1
        self.showTime(self.time)

    def DFS(self, i, j, start0):
        # 改.status，画UI
        if self.mineLabel[i][j].status == 0:
            self.mineLabel[i][j].status = 1
            self.boardofGame[i][j] = self.mineLabel[i][j].num
            if self.mineLabel[i][j].num >= 0:
                if not self.timeStart:
                    self.timeStart = True
                    self.timer.start()
                self.mineLabel[i][j].setPixmap(self.pixmapNum[self.mineLabel[i][j].num])
            if self.isGameFinished():
                self.gameWin()
            if self.mineLabel[i][j].num == 0:
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if not self.outOfBorder(r, c) and self.mineLabel[r][c].status == 0:
                            self.DFS(r, c, start0)

    def mineAreaLeftRelease(self, i, j):
        if not self.finish:
            pixmap = QPixmap(self.pixmapNum[14])
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
        if self.leftHeld:
            self.leftHeld = False  # 防止双击中的左键弹起被误认为真正的左键弹起
            if not self.outOfBorder(i, j):
                # 鼠标按住并移出局面时，索引会越界
                if self.mineLabel[i][j].status == 0 and not self.finish:
                    self.mineLabel[i][j].setPixmap(self.pixmapNum[9])

                    if not self.gamestart:
                        self.operationStream = [self.operationStream[-1]] + [('l2', (i, j))]  # 初始化并记录鼠标动作
                        # 生成的图要保证点一下不能直接获胜，所以在这里埋雷
                        self.layMine(i, j)
                        self.gamestart = True
                        self.boardofGame = minesweeper_master.refreshBoard(self.board, self.boardofGame, [(i, j)])
                        self.DFS(i, j, self.mineLabel[i][j].num == 0)
                        self.startTime = time.time()
                    elif not self.finish:
                        self.operationStream.append(('l2', (i, j)))  # 记录鼠标动作
                        self.mineLabel, self.boardofGame, failflag = minesweeper_master.ai(self.mineLabel,
                                                                                           self.boardofGame,
                                                                                           self.gameMode, i, j)
                        if not failflag:
                            self.DFS(i, j, self.mineLabel[i][j].num == 0)
                        else:
                            self.mineLabel[i][j].status = 3
                            self.gameFailed()
                        if self.isGameFinished() and not failflag:
                            self.gameWin()
        if self.gameWinFlag:
            self.showScores()
                            
    def mineAreaRightRelease(self, i, j):
        if not self.finish:
            self.operationStream.append(('r2', (i, j)))  # 记录鼠标动作
            pixmap = QPixmap(self.pixmapNum[14])
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
    
    def mineAreaRightPressed(self, i, j):
        if not self.finish:
            self.operationStream.append(('r1', (i, j)))  # 记录鼠标动作
            pixmap = QPixmap(self.pixmapNum[15])
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            if self.mineLabel[i][j].status == 0:  # 标雷
                pixmap = QPixmap(self.pixmapNum[10])
                self.mineLabel[i][j].setPixmap(pixmap)
                self.mineLabel[i][j].setScaledContents(True)
                self.mineLabel[i][j].status = 2
                # self.boardofGame[i][j] = 11
                self.mineUnFlagedNum -= 1
                self.showMineNum(self.mineUnFlagedNum)
            elif self.mineLabel[i][j].status == 2:  # 取消标雷
                self.mineLabel[i][j].setPixmap(self.pixmapNum[9])
                self.mineLabel[i][j].status = 0
                # self.boardofGame[i][j] = 10
                self.mineUnFlagedNum += 1
                self.showMineNum(self.mineUnFlagedNum)

    def mineAreaLeftPressed(self, i, j):
        self.leftHeld = True
        self.oldCell = (i, j)
        if not self.finish:
            self.operationStream.append(('l1', (i, j)))  # 记录鼠标动作
            pixmap = QPixmap(self.pixmapNum[15])
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            if self.mineLabel[i][j].status == 0:
                self.mineLabel[i][j].setPixmap(self.pixmapNum[0])

    def mineAreaLeftAndRightPressed(self, i, j):
        self.leftAndRightHeld = True
        self.oldCell = (i, j)
        if not self.finish:
            self.operationStream.append(('c1', (i, j)))  # 记录鼠标动作
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if not self.outOfBorder(r, c):
                        if self.mineLabel[r][c].status == 0:
                            self.mineLabel[r][c].setPixmap(self.pixmapNum[0])

    def chordingFlag(self, i, j):
        # i, j 周围标雷数是否满足双击的要求
        if not self.finish:
            if self.mineLabel[i][j].status == 1:
                count = 0
                for r in range(i - 1, i + 2):
                    for c in range(j - 1, j + 2):
                        if not self.outOfBorder(r, c):
                            if self.mineLabel[r][c].status == 2:
                                count += 1
                if count == 0:
                    return False
                else:
                    return count == self.mineLabel[i][j].num
            else:
                return False

    def mineAreaLeftAndRightRelease(self, i, j):
        self.leftAndRightHeld = False
        self.leftHeld = False
        if not self.finish:
            self.operationStream.append(('c2', (i, j)))  # 记录鼠标动作
            pixmap = QPixmap(self.pixmapNum[14])
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
        if not self.outOfBorder(i, j) and not self.finish:
            # 鼠标按住并移出局面时，索引会越界
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if not self.outOfBorder(r, c):
                        if self.mineLabel[r][c].status == 0:
                            self.mineLabel[r][c].setPixmap(self.pixmapNum[9])

            if not self.finish:
                if self.mineLabel[i][j].status == 1:
                    if self.chordingFlag(i, j):
                        Fail = False
                        for r in range(i - 1, i + 2):
                            for c in range(j - 1, j + 2):
                                if not self.outOfBorder(r, c):
                                    if self.mineLabel[r][c].status == 0:
                                        if self.mineLabel[r][c].num >= 0:
                                            self.DFS(r, c, self.mineLabel[r][c].num == 0)
                                        else:
                                            Fail = True
                        if Fail:
                            for r in range(i - 1, i + 2):
                                for c in range(j - 1, j + 2):
                                    if not self.outOfBorder(r, c):
                                        if self.mineLabel[r][c].status == 0 and self.mineLabel[r][c].num == -1:
                                            self.mineLabel[r][c].setPixmap(self.pixmapNum[11])
                                            self.mineLabel[r][c].status = 3
                            self.gameFailed()
        if self.gameWinFlag:
            self.showScores()

    def mineMouseMove(self, i, j):
        if not self.finish:
            if not self.outOfBorder(i, j):
                if (i, j) != self.oldCell and (self.leftAndRightHeld or self.leftHeld):
                    ii, jj = self.oldCell
                    self.oldCell = (i, j)
                    if self.leftAndRightHeld:
                        for r in range(ii - 1, ii + 2):
                            for c in range(jj - 1, jj + 2):
                                if not self.outOfBorder(r, c):
                                    if self.mineLabel[r][c].status == 0:
                                        self.mineLabel[r][c].setPixmap(self.pixmapNum[9])
                        for r in range(i - 1, i + 2):
                            for c in range(j - 1, j + 2):
                                if not self.outOfBorder(r, c):
                                    if self.mineLabel[r][c].status == 0:
                                        self.mineLabel[r][c].setPixmap(self.pixmapNum[0])

                    elif self.leftHeld:
                        if self.mineLabel[i][j].status == 0:
                            self.mineLabel[i][j].setPixmap(self.pixmapNum[0])
                        if self.mineLabel[ii][jj].status == 0:
                            self.mineLabel[ii][jj].setPixmap(self.pixmapNum[9])
            else:
                if self.leftAndRightHeld or self.leftHeld:
                    ii, jj = self.oldCell
                    if self.leftAndRightHeld:
                        for r in range(ii - 1, ii + 2):
                            for c in range(jj - 1, jj + 2):
                                if not self.outOfBorder(r, c):
                                    if self.mineLabel[r][c].status == 0:
                                        self.mineLabel[r][c].setPixmap(self.pixmapNum[9])
                    elif self.leftHeld:
                        if self.mineLabel[ii][jj].status == 0:
                            self.mineLabel[ii][jj].setPixmap(self.pixmapNum[9])

    def gameStart(self):  # 画界面，但是不埋雷
        for i in self.mineLabel:
            for j in i:
                self.gridLayout.removeWidget(j)
                sip.delete(j)
        self.mineUnFlagedNum = self.mineNum  # 没有标出的雷，显示在左上角
        self.showMineNum(self.mineUnFlagedNum)    # 在左上角画雷数
        pixmap = QPixmap(self.pixmapNum[14])
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.time = 0
        self.showTime(self.time)
        self.timeStart = False
        self.finish = False
        self.timer.stop()
        self.mineLabel.clear()
        self.mineLabel = []
        self.initMineArea()
        self.gamestart = False
        self.mainWindow.setMinimumSize(0, 0)
        self.mainWindow.resize(self.mainWindow.minimumSize())
        self.board = [[0] * self.column for _ in range(self.row)]
        self.operationStream = []  # 记录整局的鼠标操作流，格式为[('l1',(x,y)),('r1',(x,y)),('c2',(x,y))]
        self.boardofGame = [[10] * self.column for _ in range(self.row)]
        # 把窗口尽量缩小，以免从高级改成中级时窗口不能缩小

    def gameRestart(self):  # 画界面，但是不埋雷，改数据而不是重新生成label
        # 点击脸时调用
        self.time = 0
        self.showTime(self.time)
        self.mineUnFlagedNum = self.mineNum
        self.showMineNum(self.mineUnFlagedNum)
        pixmap = QPixmap(self.pixmapNum[14])
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        # self.label_3.setText("0.00")
        self.timeStart = False
        self.finish = False
        self.timer.stop()
        for i in range(0, self.row):
            for j in range(0, self.column):
                self.mineLabel[i][j].status = 0
                self.mineLabel[i][j].setPixmap(self.pixmapNum[9])
        self.gamestart = False
        # 把窗口尽量缩小，以免从高级改成中级时窗口不能缩小

    def gameFinished(self):  # 游戏结束画残局，停时间，改状态
        # print(self.operationStream)#调试用，否则请注释
        self.endTime = time.time()
        self.gameTime = self.endTime - self.startTime # 精确的游戏时间
        if self.gameWinFlag:
            for i in self.mineLabel:
                for j in i:
                    if j.num == -1:
                        j.setPixmap(self.pixmapNum[10])
                        # j.setScaledContents(True)
                    j.status = 1
        else:
            for ii in self.mineLabel:
                for jj in ii:
                    if jj.num == -1 or jj.status == 2 or jj.status == 3:
                        if jj.num == -1 and jj.status == 2:
                            jj.setPixmap(self.pixmapNum[10])
                        elif jj.num == -1 and jj.status == 0:
                            jj.setPixmap(self.pixmapNum[12])
                        elif jj.num != -1 and jj.status == 2:
                            jj.setPixmap(self.pixmapNum[13])
                        elif jj.status == 3:
                            jj.setPixmap(self.pixmapNum[11])
        self.timer.stop()
        self.finish = True

    def isGameFinished(self):
        for i in self.mineLabel:
            for j in i:
                if j.status == 0 and j.num != -1:
                    return False
        return True

    def gameWin(self):  # 成功后改脸和状态变量，并弹出成绩框
        pixmap = QPixmap(self.pixmapNum[17])
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.gameWinFlag = True
        self.gameFinished()

    def gameFailed(self): # 失败后改脸和状态变量
        pixmap = QPixmap(self.pixmapNum[16])
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.gameWinFlag = False
        self.gameFinished()
        
    def showMineNum(self, n):
        # 显示剩余雷数，雷数大于等于0，小于等于999，整数
        if n >= 0 and n <= 999:
            self.label_11.setPixmap(self.pixmapLEDNum[n//100])
            self.label_12.setPixmap(self.pixmapLEDNum[n//10%10])
            self.label_13.setPixmap(self.pixmapLEDNum[n%10])
            return
        elif n < 0:
            self.label_11.setPixmap(self.pixmapLEDNum[0])
            self.label_12.setPixmap(self.pixmapLEDNum[0])
            self.label_13.setPixmap(self.pixmapLEDNum[0])
            return
        elif n >= 1000:
            self.label_11.setPixmap(self.pixmapLEDNum[9])
            self.label_12.setPixmap(self.pixmapLEDNum[9])
            self.label_13.setPixmap(self.pixmapLEDNum[9])
            return
         
    def showTime(self, t):
        # 显示剩余时间，时间数大于等于0，小于等于999秒，整数
        if t >= 0 and t <= 999:
            self.label_31.setPixmap(self.pixmapLEDNum[t//100])
            self.label_32.setPixmap(self.pixmapLEDNum[t//10%10])
            self.label_33.setPixmap(self.pixmapLEDNum[t%10])
            return
        elif t >= 1000:
            return
    
    def actionChecked(self, k):
        # 菜单前面打勾
        self.actionchu_ji.setChecked(False)
        self.actionzhogn_ji.setChecked(False)
        self.actiongao_ji.setChecked(False)
        self.actionzi_ding_yi.setChecked(False)
        if k == 'B':
            self.actionchu_ji.setChecked(True)
        elif k == 'I':
            self.actionzhogn_ji.setChecked(True)
        elif k == 'E':
            self.actiongao_ji.setChecked(True)
        elif k == 'C':
            self.actionzi_ding_yi.setChecked(True)

    def action_BEvent(self):
        self.actionChecked('B')
        conf = configparser.ConfigParser()
        conf.read('gameSetting.ini')
        if conf['DEFAULT']['gameDifficult'] == 'B':
            self.gameRestart()
        else:
        #if self.row != 8 or self.column != 8 or self.mineNum != 10:
            self.row = 8
            self.column = 8
            self.mineNum = 10
            conf = configparser.ConfigParser()
            conf.read("gameSetting.ini")
            conf.set("DEFAULT", "gamedifficult", 'B')
            self.min3BV = conf.getint('BEGINNER', 'min3BV')
            self.max3BV = conf.getint('BEGINNER', 'max3BV')
            conf.write(open('gameSetting.ini', "w"))
            self.gameStart()
        #else:
        #    self.gameRestart()

    def action_IEvent(self):
        self.actionChecked('I')
        conf = configparser.ConfigParser()
        conf.read('gameSetting.ini')
        if conf['DEFAULT']['gameDifficult'] == 'I':
            self.gameRestart()
        else:
        #if self.row != 16 or self.column != 16 or self.mineNum != 40:
            self.row = 16
            self.column = 16
            self.mineNum = 40
            conf = configparser.ConfigParser()
            conf.read("gameSetting.ini")
            conf.set("DEFAULT", "gamedifficult", 'I')
            self.min3BV = conf.getint('INTERMEDIATE', 'min3BV')
            self.max3BV = conf.getint('INTERMEDIATE', 'max3BV')
            conf.write(open('gameSetting.ini', "w"))
            self.gameStart()
        #else:
        #    self.gameRestart()

    def action_Event(self):
        self.actionChecked('E')
        conf = configparser.ConfigParser()
        conf.read('gameSetting.ini')
        if conf['DEFAULT']['gameDifficult'] == 'E':
            self.gameRestart()
        else:
        #if self.row != 16 or self.column != 30 or self.mineNum != 99:
            self.row = 16
            self.column = 30
            self.mineNum = 99
            conf = configparser.ConfigParser()
            conf.read("gameSetting.ini")
            conf.set("DEFAULT", "gamedifficult", 'E')
            self.min3BV = conf.getint('EXPERT', 'min3BV')
            self.max3BV = conf.getint('EXPERT', 'max3BV')
            conf.write(open('gameSetting.ini', "w"))
            self.gameStart()
        #else:
        #    self.gameRestart()

    def action_CEvent(self):
        # 点击菜单栏的自定义后回调
        self.actionChecked('C')
        ui = selfDefinedParameter.Ui_Dialog(self.row, self.column,
                                            self.mineNum)
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()
        if ui.alter:
            self.row = ui.row
            self.column = ui.column
            self.mineNum = ui.mineNum
            self.min3BV = 2
            self.max3BV = 500
            conf = configparser.ConfigParser()
            conf.read("gameSetting.ini")
            conf.set("DEFAULT", "gamedifficult", 'C')
            conf.set("CUSTOM", "x", str(self.row))
            conf.set("CUSTOM", "y", str(self.column))
            conf.set("CUSTOM", "n", str(self.mineNum))
            conf.set("CUSTOM", "min3BV", str(self.min3BV))
            conf.set("CUSTOM", "max3BV", str(self.max3BV))
            conf.write(open('gameSetting.ini', "w"))
            self.gameStart()

    def action_NEvent(self):
        self.actionChecked('N')
        ui = gameSettings.Ui_Form()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()
        if ui.alter:
            #self.min3BV = ui.min3BV
            #self.max3BV = ui.max3BV
            #self.timesLimit = ui.timesLimit
            #self.enuLimit = ui.enuLimit
            self.gameMode = ui.gameMode
            self.transparency = ui.transparency / 100
            self.pixSize = ui.pixSize
            self.pixmapNum, self.pixmapLEDNum = self.importPic(self.pixSize)
            self.gameStart()
            self.mainWindow.setWindowOpacity(self.transparency)

    def action_QEvent(self):
        # 本地战绩
        self.actionChecked('Q')
        ui = gameRank.Ui_MainWindow()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()
    '''
    def action_QEvent(self):
        # 其他设置
        self.actionChecked('Q')
        ui = gameSetMoreGUI.Ui_Form()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()
    '''

    def action_HEvent(self):
        # 词典，即游戏帮助、术语表
        self.actionChecked('H')
        ui = gameTerms.Ui_Form()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()

    def action_AEvent(self):
        # 关于
        self.actionChecked('A')
        ui = gameAbout.Ui_Form()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()

    def action_JEvent(self):
        # 入门教程
        self.actionChecked('J')
        ui = gameHelp.Ui_Form()
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()

    '''
    def openBrowser(self, k):
        #打开内置的浏览器，一共有3个浏览器，参数都在配置文件里临时读
        ui = browserGUI.Ui_Form(k)h
        ui.Dialog.setModal(True)
        ui.Dialog.show()
        ui.Dialog.exec_()
    '''

    def showScores(self):
        # 游戏结束后，按空格展示成绩
        if self.finish:
            scores = minesweeper_master.calScores(self.gameMode, self.gameWinFlag, self.gameTime,
                                                  self.operationStream, self.board)
            ui = gameScores.Ui_Form(scores)
            ui.Dialog.setModal(True)
            ui.Dialog.show()
            ui.Dialog.exec_()












