@echo off
call pyuic4 window.ui -o windowUi.py
call pyuic4 addrundown.ui -o Rundown.py
call pyrcc4 icons.qrc -o icons_rc.py