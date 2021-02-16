from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mainWindowGUI
import mineSweeperGUI

# import sweeper
if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
    # app.aboutToQuit.connect(app.deleteLater)
    mainWindow = mainWindowGUI.MainWindow ()
    ui = mineSweeperGUI.MineSweeperGUI (mainWindow)
    mainWindow.show()
    sys.exit (app.exec_())



#bug:
#    自定义模式的鲁棒性
#    生成无猜局面时增加一种鲁棒的“快速模式”
#    生成极端bv局面时采用鲁棒的“快速模式”，仅对标准模式有效？
#    可选择的无猜局面算法（筛选算法或修改算法）
#    快速给出多变量方程的一个解的算法
#    计算每格概率的子函数
#    “可能在标记双击未打开局面时，按下方格的阴影没有恢复”
#    局面要重写，抽象不够
#    加入AI模式
#    自动重开、自动弹成绩、获胜弹成绩等可选的功能
#    更快的枚举算法
#    浏览器打包后会崩溃（按4、5、6键会崩）（还没想好怎么改）
#    改级别时会闪（还没想好怎么改）





