from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import gameEntrance
import mainWindowGUI
import mineSweeperGUI

# import sweeper
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.aboutToQuit.connect(app.deleteLater)
    ui = gameEntrance.Ui_Form()
    ui.Dialog.setModal(True)
    ui.Dialog.show()
    ui.Dialog.exec_()
    if gameEntrance.Flag():
        mainWindow = mainWindowGUI.MainWindow()
        ui = mineSweeperGUI.MineSweeperGUI(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())

