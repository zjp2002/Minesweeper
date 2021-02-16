@echo off
pyuic5 -o gameAbout.py ui_about.ui
pyuic5 -o gameSettings.py ui_gs.ui
pyuic5 -o superGUI.py main_board.ui
pyuic5 -o gameHelp.py ui_help.ui
pyuic5 -o gameSetMoreGUI.py ui_gs_more.ui
pyuic5 -o browserGUI.py ui_browser.ui
pyuic5 -o gameTerms.py ui_terms.ui
pyuic5 -o gameScores.py ui_scores.ui
pause