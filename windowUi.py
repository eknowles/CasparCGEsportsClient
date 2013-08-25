# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Fri Aug 23 02:43:37 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1027, 738)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Graphics/Images/A.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("/*\n"
" * General.\n"
" */\n"
"*::indicator\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"*::indicator:checked\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxChecked.png);\n"
"}\n"
"*::menu-indicator\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowDown.png);\n"
"}\n"
"*::down-arrow\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowDown.png);\n"
"}\n"
"*::down-arrow:disabled\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowDownDisabled.png);\n"
"}\n"
"*::down-arrow:off\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowDownDisabled.png);\n"
"}\n"
"*::up-arrow\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowUp.png);\n"
"}\n"
"*::up-arrow:disabled\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowUpDisabled.png);\n"
"}\n"
"*::up-arrow:off\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowUpDisabled.png);\n"
"}\n"
"*::left-arrow\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowLeft.png);\n"
"}\n"
"*::left-arrow:disabled\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowLeftDisabled.png);\n"
"}\n"
"*::left-arrow:off\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowLeftDisabled.png);\n"
"}\n"
"*::right-arrow\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowRight.png);\n"
"}\n"
"*::right-arrow:disabled\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowRightDisabled.png);\n"
"}\n"
"*::right-arrow:off\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowRightDisabled.png);\n"
"}\n"
"\n"
"\n"
"/*\n"
" * QWidget\n"
" */\n"
"QWidget\n"
"{\n"
"    alternate-background-color: rgba(55, 55, 55, 255);\n"
"    background-color: rgba(64, 64, 64, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 2px;\n"
"    border-style: solid;\n"
"    color: rgba(255, 255, 255, 255);\n"
"    selection-background-color: rgba(80, 80, 80, 255);\n"
"    selection-color: rgba(255, 255, 255, 255);\n"
"}\n"
"QWidget:disabled\n"
"{\n"
"    color: rgba(128, 128, 128, 255);\n"
"}\n"
"\n"
"/*\n"
" * QFrame\n"
" */\n"
"QFrame\n"
"{\n"
"   background-color: rgba(64, 64, 64, 255);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/*\n"
" * QCheckBox\n"
" */\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QCheckBox::indicator\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"/*QCheckBox::indicator:unchecked\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxUnchecked.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxUncheckedHover.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxUncheckedPressed.png);\n"
"}*/\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxChecked.png);\n"
"}\n"
"/*QCheckBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxCheckedHover.png);\n"
"}\n"
"QCheckBox::indicator:checked:pressed\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxCheckedPressed.png);\n"
"}\n"
"QCheckBox::indicator:indeterminate:hover\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxIndeterminateHover.png);\n"
"}\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/Graphics/Images/CheckboxIndeterminatePressed.png);\n"
"}*/\n"
"\n"
"/*\n"
" * QRadioButton\n"
" */\n"
"QRadioButton\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"/*QRadioButton::indicator::unchecked\n"
"{\n"
"    image: url(:/Graphics/Images/RadiobuttonUnchecked.png);\n"
"}\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/Graphics/Images/RadiobuttonUnchecked_hover.png);\n"
"}\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"    image: url(:/Graphics/Images/RadiobuttonUncheckedPressed.png);\n"
"}*/\n"
"QRadioButton::indicator::checked\n"
"{\n"
"    image: url(:/Graphics/Images/RadiobuttonChecked.png);\n"
"}\n"
"/*QRadioButton::indicator:checked:hover\n"
"{\n"
"    image: url(:/Graphics/Images/RadiobuttonCheckedHover.png);\n"
"}\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"    image: url(:/Graphics/Images/RadiobuttonCheckedPressed.png);\n"
"}*/\n"
"\n"
"/*\n"
" * QSplitter\n"
" */\n"
"QSplitter::handle:vertical\n"
"{\n"
"    image: url(:/Graphics/Images/SplitterVertical.png);\n"
"}\n"
"QSplitter::handle:horizontal\n"
"{\n"
"    image: url(:/Graphics/Images/SplitterHorizontal.png);\n"
"}\n"
"\n"
"/*\n"
" * QLCDNumber\n"
" */\n"
"QLCDNumber\n"
"{\n"
"    background-color: transparent;\n"
"    color: rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"/*\n"
" * QStatusBar\n"
" */\n"
"QStatusBar\n"
"{\n"
"    min-height: 22px;\n"
"}\n"
"\n"
"/*\n"
" * QListView\n"
" */\n"
"QListView\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"/*\n"
" * QLineEdit\n"
" */\n"
"QLineEdit\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"    min-height: 20px;\n"
"}\n"
"QLineEdit::disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*\n"
" * QTextEdit\n"
" */\n"
"QTextEdit\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"}\n"
"QTextEdit::disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*\n"
" * QPlainTextEdit\n"
" */\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"}\n"
"QPlainTextEdit::disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*\n"
" * QToolBar\n"
" */\n"
"QToolBar\n"
"{\n"
"    border-radius: 0px;\n"
"    padding: 1px;\n"
"}\n"
"QToolBar QToolButton\n"
"{\n"
"    background-color: transparent;\n"
"    border-width: 0px;\n"
"}\n"
"QToolBar QToolButton:hover\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QToolBar::handle:vertical\n"
"{\n"
"    margin-top: 4px;\n"
"    image: url(:/Graphics/Images/ToolbarSplitterVertical.png);\n"
"}\n"
"QToolBar::handle:horizontal\n"
"{\n"
"    margin-left: 4px;\n"
"    image: url(:/Graphics/Images/ToolbarSplitterHorizontal.png);\n"
"}\n"
"\n"
"\n"
"/*\n"
" * QToolTip\n"
" */\n"
"QToolTip\n"
"{\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"/*\n"
" * QSizeGrip\n"
" */\n"
"QSizeGrip\n"
"{\n"
"    background-color: rgba(60, 60, 60, 255);\n"
"    border-bottom-left-radius: 0px;\n"
"    border-left-width: 1px;\n"
"    border-top-right-radius: 0px;\n"
"    border-top-width: 1px;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"}\n"
"\n"
"/*\n"
" * QGroupBox\n"
" */\n"
"QGroupBox\n"
"{\n"
"    border-width: 1px;\n"
"    margin: 4px;\n"
"    padding: 2px;\n"
"}\n"
"QGroupBox::title\n"
"{\n"
"    left: 5px;\n"
"    padding: 7px;\n"
"    subcontrol-origin: border;\n"
"    top: -1.7ex;\n"
"}\n"
"\n"
"/*\n"
" * QAbstractItemView\n"
" */\n"
"QAbstractItemView\n"
"{\n"
"    outline: 0;\n"
"}\n"
"\n"
"/*\n"
" * QTreeView\n"
" */\n"
"QTreeView\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"}\n"
"QTreeView::item:selected\n"
"{\n"
"    background-color: rgba(80, 80, 80, 255);\n"
"    color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTreeView::branch\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QTreeView::branch:closed:has-children\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowRight.png);\n"
"}\n"
"QTreeView::branch:open:has-children\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowDown.png);\n"
"}\n"
"\n"
"/*\n"
" * QTreeWidget\n"
" */\n"
"QTreeWidget\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"}\n"
"QTreeWidget::item:selected\n"
"{\n"
"    background-color: rgba(80, 80, 80, 255);\n"
"    color: rgba(255, 255, 255, 255);\n"
"}\n"
"QTreeWidget::branch\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QTreeWidget::branch:closed:has-children\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowRight.png);\n"
"}\n"
"QTreeWidget::branch:open:has-children\n"
"{\n"
"    image: url(:/Graphics/Images/ArrowDown.png);\n"
"}\n"
"\n"
"/*\n"
" * QTableWidget\n"
" */\n"
"QTableWidget\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"}\n"
"QTableWidget::item:selected\n"
"{\n"
"    background-color: rgba(80, 80, 80, 255);\n"
"    color: rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"/*\n"
" * QProgressBar\n"
" */\n"
"QProgressBar\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"}\n"
"QProgressBar::chunk:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*\n"
" * QMenuBar\n"
" */\n"
"QMenuBar\n"
"{\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));*/\n"
"    background-color: rgba(64, 64, 64, 255);\n"
"    border-bottom-width: 1px;\n"
"    border-radius: 0px;\n"
"}\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: rgba(60, 60, 60, 255); /* When selected using mouse or keyboard. */\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: rgba(60, 60, 60, 255);\n"
"}\n"
"\n"
"/*\n"
" * QMenu\n"
" */\n"
"QMenu\n"
"{\n"
"    background-color: rgba(60, 60, 60, 255);\n"
"    border-radius: 0px;\n"
"    border-width: 1px;\n"
"}\n"
"QMenu::icon\n"
"{\n"
"    left: 5px;\n"
"}\n"
"QMenu::item\n"
"{\n"
"    padding-bottom: 4px;\n"
"    padding-left: 25px;\n"
"    padding-right: 19px;\n"
"    padding-top: 3px;\n"
"}\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: rgba(80, 80, 80, 255);\n"
"}\n"
"\n"
"/*\n"
" * QToolBox\n"
" */\n"
"QToolBox\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 2px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"QToolBox::tab\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-bottom-width: 1px;\n"
"    border-top-width: 1px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
" }\n"
"QToolBox::tab:first\n"
"{\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    border-top-width: 0px;\n"
"}\n"
"QToolBox::tab:last\n"
"{\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"    border-bottom-width: 0px;\n"
"}\n"
"QToolBox::tab:only-one\n"
"{\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    border-top-width: 0px;\n"
"}\n"
"QToolBox::tab:selected\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-width: 1px;\n"
"}\n"
"QToolBox::tab:selected:disabled\n"
"{\n"
"    background-color: transparent;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-width: 1px;\n"
"}\n"
"QToolBox::tab:!selected:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"/*\n"
" * QPushButton\n"
" */\n"
"QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-width: 1px;\n"
"    padding-bottom: 4px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"}\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"QMessageBox QPushButton\n"
"{\n"
"    min-width: 54px;\n"
"}\n"
"\n"
"QFileDialog QPushButton\n"
"{\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"#controller QPushButton\n"
"{\n"
"    font: 75 15pt \"DINPro-Bold\";\n"
"    border-width: 1px;\n"
"    padding-bottom: 4px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"}\n"
"\n"
"#controller #con_scedule QPushButton { border-color: rgba(244,140,54,255); }\n"
"#controller #con_team QPushButton { border-color: rgba(31,162,244,255); }\n"
"#controller #con_player QPushButton { border-color: rgba(222,102,44,255); }\n"
"#controller #con_event QPushButton { border-color: rgba(5,105,206,255); }\n"
"#controller #con_twitter QPushButton { border-color: rgba(170,221,255,255); }\n"
"\n"
"#controller #con_scedule QPushButton:checked { background-color: rgba(244,140,54,255); }\n"
"#controller #con_team QPushButton:checked { background-color: rgba(31,162,244,255); }\n"
"#controller #con_player QPushButton:checked { background-color: rgba(222,102,44,255); }\n"
"#controller #con_event QPushButton:checked { background-color: rgba(5,105,206,255); }\n"
"#controller #con_twitter QPushButton:checked { background-color: rgba(170,221,255,255); }\n"
"\n"
"\n"
"/*\n"
" * QToolButton\n"
" */\n"
"QToolButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-width: 1px;\n"
"}\n"
"QToolButton:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QToolButton:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QToolButton::menu-indicator\n"
"{\n"
"    image: none;\n"
"}\n"
"\n"
"/*\n"
" * QComboBox\n"
" */\n"
"QComboBox\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-width: 1px;\n"
"    min-height: 20px;\n"
"    padding-left: 5px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover, QComboBox::drop-down:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"    border-left-color: rgba(42, 42, 42, 255);\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-top-width: 0px;\n"
"}\n"
"QComboBox:editable:on\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: rgba(60, 60, 60, 255);\n"
"    border-radius: 0px;\n"
"    padding-left: 2px;\n"
"}\n"
"\n"
"/*\n"
" * QSpinBox\n"
" */\n"
"QSpinBox\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"}\n"
"QSpinBox::up-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-width: 1px;\n"
"    border-left-width: 1px;\n"
"    border-top-right-radius: 2px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: top right;\n"
"}\n"
"QSpinBox::up-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QSpinBox::up-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QSpinBox::up-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QSpinBox::down-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-right-radius: 2px;\n"
"    border-left-width: 1px;\n"
"    border-top-width: 1px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"QSpinBox::down-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QSpinBox::down-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QSpinBox::down-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"/*\n"
" * QDoubleSpinBox\n"
" */\n"
"QDoubleSpinBox\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"}\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-width: 1px;\n"
"    border-left-width: 1px;\n"
"    border-top-right-radius: 2px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: top right;\n"
"}\n"
"QDoubleSpinBox::up-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QDoubleSpinBox::up-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-right-radius: 2px;\n"
"    border-left-width: 1px;\n"
"    border-top-width: 1px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"QDoubleSpinBox::down-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QDoubleSpinBox::down-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"/*\n"
" * QDateEdit\n"
" */\n"
"QDateEdit\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"}\n"
"QDateEdit::up-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-width: 1px;\n"
"    border-left-width: 1px;\n"
"    border-top-right-radius: 2px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: top right;\n"
"}\n"
"QDateEdit::up-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QDateEdit::up-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDateEdit::up-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDateEdit::down-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-right-radius: 2px;\n"
"    border-left-width: 1px;\n"
"    border-top-width: 1px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"QDateEdit::down-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QDateEdit::down-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDateEdit::down-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"/*\n"
" * QTimeEdit\n"
" */\n"
"QTimeEdit\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"}\n"
"QTimeEdit::up-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-width: 1px;\n"
"    border-left-width: 1px;\n"
"    border-top-right-radius: 2px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: top right;\n"
"}\n"
"QTimeEdit::up-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QTimeEdit::up-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QTimeEdit::up-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QTimeEdit::down-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-right-radius: 2px;\n"
"    border-left-width: 1px;\n"
"    border-top-width: 1px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"QTimeEdit::down-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QTimeEdit::down-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QTimeEdit::down-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"/*\n"
" * QDateTimeEdit\n"
" */\n"
"QDateTimeEdit\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-width: 1px;\n"
"    min-height: 20px;\n"
"    min-width: 50px;\n"
"}\n"
"QDateTimeEdit::up-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-width: 1px;\n"
"    border-left-width: 1px;\n"
"    border-top-right-radius: 2px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: top right;\n"
"}\n"
"QDateTimeEdit::up-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDateTimeEdit::down-button\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-bottom-right-radius: 2px;\n"
"    border-left-width: 1px;\n"
"    border-top-width: 1px;\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    subcontrol-position: bottom right;\n"
"}\n"
"QDateTimeEdit::down-button:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"/*\n"
" * QTabWidget / QTabBar\n"
" */\n"
"QTabWidget::pane\n"
"{\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 2px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    position: absolute;\n"
"    top: -1px;\n"
"}\n"
"QTabWidget::tab-bar\n"
"{\n"
"    left: 0px;\n"
"}\n"
"QTabBar\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QTabBar::tab\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    border-width: 1px;\n"
"    padding-bottom: 3px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    padding-top: 3px;\n"
"    margin-left: -1px;\n"
"    min-height: 16px;\n"
"}\n"
"QTabBar::tab:only-one\n"
"{\n"
"    margin: 0; /* If there is only one tab, we don\'t want overlapping margins. */\n"
"}\n"
"QTabBar::tab:first\n"
"{\n"
"    margin-left: 0; /* The first selected tab has nothing to overlap on the left. */\n"
"}\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"    border-bottom-width: 0px;\n"
"    padding-bottom: 4px;\n"
"}\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"    background-color: transparent;\n"
"    border-bottom-width: 0px;\n"
"}\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QTabBar::close-button\n"
"{\n"
"    image: url(:/Graphics/Images/Close.png);\n"
"}\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/Graphics/Images/CloseHover.png);\n"
"}\n"
"QTabBar QToolButton\n"
"{\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 2px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"\n"
"/*\n"
" * QHeaderView\n"
" */\n"
"QHeaderView::section\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 1px;\n"
"    border-style: solid;\n"
"    min-height: 14px;\n"
"    padding: 4px;\n"
"}\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QHeaderView::section:first\n"
"{\n"
"    border-top-left-radius: 2px;\n"
"}\n"
"QHeaderView::section:last\n"
"{\n"
"    border-right-width: 0px; /* The last header section has no border to the right. */\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"QHeaderView::section:only-one\n"
"{\n"
"    border-right-width: 0px; /* The is only one header section with no border to the right. */\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"QHeaderView::section:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QHeaderView::section:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"\n"
"/*\n"
" * QScrollBar\n"
" */\n"
"QScrollBar:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(55, 55, 55, 255), stop:1 rgba(42, 42, 42, 255));\n"
"    height: 12px;\n"
"}\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-top-width: 1px;\n"
"    border-left-width: 1px;\n"
"    border-radius: 6px;\n"
"    border-right-width: 1px;\n"
"    min-width: 21px;\n"
"}\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"QScrollBar:left-arrow:horizontal\n"
"{\n"
"    image: none;\n"
"}\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: none;\n"
"}\n"
"QScrollBar::add-page:horizontal\n"
"{\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-top-width: 1px;\n"
"}\n"
"QScrollBar::sub-page:horizontal\n"
"{\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-top-width: 1px;\n"
"}\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(42, 42, 42, 255), stop:1 rgba(55, 55, 55, 255));\n"
"    width: 12px;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(80, 80, 80, 255), stop:1 rgba(60, 60, 60, 255));\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-style: solid;\n"
"    border-top-width: 1px;\n"
"    border-left-width: 1px;\n"
"    border-bottom-width: 1px;\n"
"    border-radius: 6px;\n"
"    min-height: 21px;\n"
"}\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border-width: 0px;\n"
"}\n"
"QScrollBar:up-arrow:vertical\n"
"{\n"
"    image: none;\n"
"}\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: none;\n"
"}\n"
"QScrollBar::add-page:vertical\n"
"{\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-left-width: 1px;\n"
"    border-style: solid;\n"
"}\n"
"QScrollBar::sub-page:vertical\n"
"{\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-left-width: 1px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"/*\n"
" * QSlider\n"
" */\n"
" QSlider\n"
" {\n"
"     background-color: transparent;\n"
" }\n"
"QSlider::groove\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 2px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"QSlider::sub-page\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 2px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"QSlider::add-page\n"
"{\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 2px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"QSlider::handle\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(80, 80, 80, 255));\n"
"    border-color: rgba(42, 42, 42, 255);\n"
"    border-radius: 0px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"}\n"
"QSlider::handle:hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QSlider::handle:pressed\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(90, 90, 90, 255));\n"
"}\n"
"QSlider::handle:disabled\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"QSlider::groove:vertical\n"
"{\n"
"    width: 3px;\n"
"}\n"
"QSlider::sub-page:vertical\n"
"{\n"
"    width: 6px;\n"
"}\n"
"QSlider::add-page:vertical\n"
"{\n"
"    width: 6px;\n"
"}\n"
"QSlider::handle:vertical\n"
"{\n"
"    height: 6px;\n"
"    margin-left: -6px;\n"
"    margin-right: -6px;\n"
"}\n"
"QSlider::groove:horizontal\n"
"{\n"
"    height: 3px;\n"
"}\n"
"QSlider::sub-page:horizontal\n"
"{\n"
"    height: 6px;\n"
"}\n"
"QSlider::add-page:horizontal\n"
"{\n"
"    height: 6px;\n"
"}\n"
"QSlider::handle:horizontal\n"
"{\n"
"    width: 6px;\n"
"    margin-top: -6px;\n"
"    margin-bottom: -6px;\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_8)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.controller = QtGui.QWidget(self.tab_8)
        self.controller.setObjectName(_fromUtf8("controller"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.controller)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.con_scedule = QtGui.QWidget(self.controller)
        self.con_scedule.setObjectName(_fromUtf8("con_scedule"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.con_scedule)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setMargin(5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.Console_ComingUp = QtGui.QPushButton(self.con_scedule)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_ComingUp.sizePolicy().hasHeightForWidth())
        self.Console_ComingUp.setSizePolicy(sizePolicy)
        self.Console_ComingUp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_ComingUp.setFont(font)
        self.Console_ComingUp.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_ComingUp.setCheckable(True)
        self.Console_ComingUp.setChecked(False)
        self.Console_ComingUp.setFlat(False)
        self.Console_ComingUp.setObjectName(_fromUtf8("Console_ComingUp"))
        self.verticalLayout_7.addWidget(self.Console_ComingUp)
        self.Console_UpNext = QtGui.QPushButton(self.con_scedule)
        self.Console_UpNext.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_UpNext.sizePolicy().hasHeightForWidth())
        self.Console_UpNext.setSizePolicy(sizePolicy)
        self.Console_UpNext.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_UpNext.setFont(font)
        self.Console_UpNext.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_UpNext.setCheckable(True)
        self.Console_UpNext.setChecked(False)
        self.Console_UpNext.setFlat(False)
        self.Console_UpNext.setObjectName(_fromUtf8("Console_UpNext"))
        self.verticalLayout_7.addWidget(self.Console_UpNext)
        self.Console_Sponsors = QtGui.QPushButton(self.con_scedule)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_Sponsors.sizePolicy().hasHeightForWidth())
        self.Console_Sponsors.setSizePolicy(sizePolicy)
        self.Console_Sponsors.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_Sponsors.setFont(font)
        self.Console_Sponsors.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_Sponsors.setCheckable(True)
        self.Console_Sponsors.setChecked(False)
        self.Console_Sponsors.setFlat(False)
        self.Console_Sponsors.setObjectName(_fromUtf8("Console_Sponsors"))
        self.verticalLayout_7.addWidget(self.Console_Sponsors)
        self.horizontalLayout_5.addWidget(self.con_scedule)
        self.con_team = QtGui.QWidget(self.controller)
        self.con_team.setObjectName(_fromUtf8("con_team"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.con_team)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setMargin(5)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.Console_TeamMatch = QtGui.QPushButton(self.con_team)
        self.Console_TeamMatch.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_TeamMatch.sizePolicy().hasHeightForWidth())
        self.Console_TeamMatch.setSizePolicy(sizePolicy)
        self.Console_TeamMatch.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_TeamMatch.setFont(font)
        self.Console_TeamMatch.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_TeamMatch.setCheckable(True)
        self.Console_TeamMatch.setChecked(False)
        self.Console_TeamMatch.setFlat(False)
        self.Console_TeamMatch.setObjectName(_fromUtf8("Console_TeamMatch"))
        self.verticalLayout_8.addWidget(self.Console_TeamMatch)
        self.Console_Players1 = QtGui.QPushButton(self.con_team)
        self.Console_Players1.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_Players1.sizePolicy().hasHeightForWidth())
        self.Console_Players1.setSizePolicy(sizePolicy)
        self.Console_Players1.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_Players1.setFont(font)
        self.Console_Players1.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_Players1.setCheckable(True)
        self.Console_Players1.setChecked(False)
        self.Console_Players1.setFlat(False)
        self.Console_Players1.setObjectName(_fromUtf8("Console_Players1"))
        self.verticalLayout_8.addWidget(self.Console_Players1)
        self.Console_Players2 = QtGui.QPushButton(self.con_team)
        self.Console_Players2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_Players2.sizePolicy().hasHeightForWidth())
        self.Console_Players2.setSizePolicy(sizePolicy)
        self.Console_Players2.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_Players2.setFont(font)
        self.Console_Players2.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_Players2.setCheckable(True)
        self.Console_Players2.setChecked(False)
        self.Console_Players2.setFlat(False)
        self.Console_Players2.setObjectName(_fromUtf8("Console_Players2"))
        self.verticalLayout_8.addWidget(self.Console_Players2)
        self.horizontalLayout_5.addWidget(self.con_team)
        self.con_player = QtGui.QWidget(self.controller)
        self.con_player.setObjectName(_fromUtf8("con_player"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.con_player)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setMargin(5)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.pushButton_30 = QtGui.QPushButton(self.con_player)
        self.pushButton_30.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        self.pushButton_30.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setChecked(False)
        self.pushButton_30.setFlat(False)
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.verticalLayout_9.addWidget(self.pushButton_30)
        self.horizontalLayout_5.addWidget(self.con_player)
        self.con_event = QtGui.QWidget(self.controller)
        self.con_event.setObjectName(_fromUtf8("con_event"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.con_event)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setMargin(5)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.Console_TweetFeed = QtGui.QPushButton(self.con_event)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_TweetFeed.sizePolicy().hasHeightForWidth())
        self.Console_TweetFeed.setSizePolicy(sizePolicy)
        self.Console_TweetFeed.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_TweetFeed.setFont(font)
        self.Console_TweetFeed.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_TweetFeed.setCheckable(True)
        self.Console_TweetFeed.setChecked(False)
        self.Console_TweetFeed.setFlat(False)
        self.Console_TweetFeed.setObjectName(_fromUtf8("Console_TweetFeed"))
        self.verticalLayout_13.addWidget(self.Console_TweetFeed)
        self.Console_TweetSingle = QtGui.QPushButton(self.con_event)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_TweetSingle.sizePolicy().hasHeightForWidth())
        self.Console_TweetSingle.setSizePolicy(sizePolicy)
        self.Console_TweetSingle.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_TweetSingle.setFont(font)
        self.Console_TweetSingle.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_TweetSingle.setCheckable(True)
        self.Console_TweetSingle.setChecked(False)
        self.Console_TweetSingle.setFlat(False)
        self.Console_TweetSingle.setObjectName(_fromUtf8("Console_TweetSingle"))
        self.verticalLayout_13.addWidget(self.Console_TweetSingle)
        self.Console_IRC = QtGui.QPushButton(self.con_event)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console_IRC.sizePolicy().hasHeightForWidth())
        self.Console_IRC.setSizePolicy(sizePolicy)
        self.Console_IRC.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Bold"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Console_IRC.setFont(font)
        self.Console_IRC.setStyleSheet(_fromUtf8("font: 75 15pt \"DINPro-Bold\";"))
        self.Console_IRC.setCheckable(True)
        self.Console_IRC.setChecked(False)
        self.Console_IRC.setFlat(False)
        self.Console_IRC.setObjectName(_fromUtf8("Console_IRC"))
        self.verticalLayout_13.addWidget(self.Console_IRC)
        self.horizontalLayout_5.addWidget(self.con_event)
        self.verticalLayout_6.addWidget(self.controller)
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.sch_left = QtGui.QWidget(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sch_left.sizePolicy().hasHeightForWidth())
        self.sch_left.setSizePolicy(sizePolicy)
        self.sch_left.setMinimumSize(QtCore.QSize(0, 50))
        self.sch_left.setMaximumSize(QtCore.QSize(420, 16777215))
        self.sch_left.setObjectName(_fromUtf8("sch_left"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.sch_left)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget_3 = QtGui.QWidget(self.sch_left)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.line = QtGui.QFrame(self.widget_3)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.label_6 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DINPro-Light"))
        font.setPointSize(48)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.formLayout = QtGui.QFormLayout(self.widget_4)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.widget_4)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2013, 8, 11), QtCore.QTime(6, 0, 0)))
        self.dateTimeEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.dateTimeEdit)
        self.label_5 = QtGui.QLabel(self.widget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBox = QtGui.QComboBox(self.widget_4)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_3 = QtGui.QLabel(self.widget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.widget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_7 = QtGui.QLabel(self.widget_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.textEdit = QtGui.QTextEdit(self.widget_4)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.textEdit)
        self.label_8 = QtGui.QLabel(self.widget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.LabelRole, self.label_8)
        self.comboBox_2 = QtGui.QComboBox(self.widget_4)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.widget_5 = QtGui.QWidget(self.widget_3)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_5 = QtGui.QPushButton(self.widget_5)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton = QtGui.QPushButton(self.widget_5)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.widget_5)
        self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_5.addWidget(self.widget_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.pushButton_2 = QtGui.QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_4 = QtGui.QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.widget_3)
        self.horizontalLayout_4.addWidget(self.sch_left)
        self.widget_6 = QtGui.QWidget(self.tab_3)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.widget_6)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_4.addWidget(self.widget_6)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.widget_10 = QtGui.QWidget(self.tab)
        self.widget_10.setObjectName(_fromUtf8("widget_10"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_10)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox_3 = QtGui.QComboBox(self.widget_10)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.verticalLayout_2.addWidget(self.comboBox_3)
        self.label = QtGui.QLabel(self.widget_10)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setMaximumSize(QtCore.QSize(300, 300))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_9.addWidget(self.widget_10)
        self.widget_11 = QtGui.QWidget(self.tab)
        self.widget_11.setObjectName(_fromUtf8("widget_11"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.widget_11)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.comboBox_4 = QtGui.QComboBox(self.widget_11)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.verticalLayout_12.addWidget(self.comboBox_4)
        self.label_2 = QtGui.QLabel(self.widget_11)
        self.label_2.setMinimumSize(QtCore.QSize(300, 300))
        self.label_2.setMaximumSize(QtCore.QSize(300, 300))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_12.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.horizontalLayout_9.addWidget(self.widget_11)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.widget = QtGui.QWidget(self.tab_4)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tweet_search_line = QtGui.QLineEdit(self.widget_2)
        self.tweet_search_line.setObjectName(_fromUtf8("tweet_search_line"))
        self.horizontalLayout_2.addWidget(self.tweet_search_line)
        self.tweetspinBox = QtGui.QSpinBox(self.widget_2)
        self.tweetspinBox.setSuffix(_fromUtf8(""))
        self.tweetspinBox.setMinimum(5)
        self.tweetspinBox.setSingleStep(5)
        self.tweetspinBox.setProperty("value", 20)
        self.tweetspinBox.setObjectName(_fromUtf8("tweetspinBox"))
        self.horizontalLayout_2.addWidget(self.tweetspinBox)
        self.get_tweets_btn = QtGui.QPushButton(self.widget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Graphics/Images/Twitter.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.get_tweets_btn.setIcon(icon1)
        self.get_tweets_btn.setObjectName(_fromUtf8("get_tweets_btn"))
        self.horizontalLayout_2.addWidget(self.get_tweets_btn)
        self.BTN_TweetSingle = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_TweetSingle.sizePolicy().hasHeightForWidth())
        self.BTN_TweetSingle.setSizePolicy(sizePolicy)
        self.BTN_TweetSingle.setMinimumSize(QtCore.QSize(0, 25))
        self.BTN_TweetSingle.setObjectName(_fromUtf8("BTN_TweetSingle"))
        self.horizontalLayout_2.addWidget(self.BTN_TweetSingle)
        self.tweetshow = QtGui.QPushButton(self.widget_2)
        self.tweetshow.setMinimumSize(QtCore.QSize(80, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Graphics/Images/Add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tweetshow.setIcon(icon2)
        self.tweetshow.setObjectName(_fromUtf8("tweetshow"))
        self.horizontalLayout_2.addWidget(self.tweetshow)
        self.pushButton_33 = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_33.setMaximumSize(QtCore.QSize(80, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Graphics/Images/Remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_33.setIcon(icon3)
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.horizontalLayout_2.addWidget(self.pushButton_33)
        self.verticalLayout_10.addWidget(self.widget_2)
        self.tweet_table = QtGui.QTableWidget(self.widget)
        self.tweet_table.setAutoFillBackground(False)
        self.tweet_table.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tweet_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.tweet_table.setLineWidth(1)
        self.tweet_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tweet_table.setDragEnabled(True)
        self.tweet_table.setAlternatingRowColors(True)
        self.tweet_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tweet_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tweet_table.setShowGrid(True)
        self.tweet_table.setWordWrap(True)
        self.tweet_table.setObjectName(_fromUtf8("tweet_table"))
        self.tweet_table.setColumnCount(0)
        self.tweet_table.setRowCount(0)
        self.tweet_table.horizontalHeader().setCascadingSectionResizes(True)
        self.tweet_table.horizontalHeader().setHighlightSections(False)
        self.tweet_table.horizontalHeader().setSortIndicatorShown(True)
        self.tweet_table.horizontalHeader().setStretchLastSection(True)
        self.tweet_table.verticalHeader().setVisible(False)
        self.tweet_table.verticalHeader().setCascadingSectionResizes(False)
        self.tweet_table.verticalHeader().setHighlightSections(False)
        self.tweet_table.verticalHeader().setSortIndicatorShown(False)
        self.tweet_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_10.addWidget(self.tweet_table)
        self.horizontalLayout_7.addWidget(self.widget)
        self.widget_7 = QtGui.QWidget(self.tab_4)
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widget_8 = QtGui.QWidget(self.widget_7)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_4.addWidget(self.widget_8)
        self.horizontalLayout_7.addWidget(self.widget_7)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_9)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_9)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_11.addWidget(self.textEdit_2)
        self.tabWidget.addTab(self.tab_9, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget_9 = QtGui.QWidget(self.centralwidget)
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.console_text = QtGui.QLineEdit(self.widget_9)
        self.console_text.setObjectName(_fromUtf8("console_text"))
        self.horizontalLayout_8.addWidget(self.console_text)
        self.console_go = QtGui.QPushButton(self.widget_9)
        self.console_go.setObjectName(_fromUtf8("console_go"))
        self.horizontalLayout_8.addWidget(self.console_go)
        self.verticalLayout.addWidget(self.widget_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionFullsreen = QtGui.QAction(MainWindow)
        self.actionFullsreen.setObjectName(_fromUtf8("actionFullsreen"))
        self.actionImport_Scedule = QtGui.QAction(MainWindow)
        self.actionImport_Scedule.setObjectName(_fromUtf8("actionImport_Scedule"))
        self.actionExport_Schedule = QtGui.QAction(MainWindow)
        self.actionExport_Schedule.setObjectName(_fromUtf8("actionExport_Schedule"))
        self.actionImport_Schedule = QtGui.QAction(MainWindow)
        self.actionImport_Schedule.setObjectName(_fromUtf8("actionImport_Schedule"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionReload_Client = QtGui.QAction(MainWindow)
        self.actionReload_Client.setObjectName(_fromUtf8("actionReload_Client"))
        self.menuFile.addAction(self.actionReload_Client)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_Schedule)
        self.menuFile.addAction(self.actionImport_Schedule)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionFullsreen)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESCG", None))
        self.Console_ComingUp.setText(_translate("MainWindow", "COMING UP", None))
        self.Console_UpNext.setText(_translate("MainWindow", "UP NEXT", None))
        self.Console_Sponsors.setText(_translate("MainWindow", "SHOW SPONSORS", None))
        self.Console_TeamMatch.setText(_translate("MainWindow", "MATCH UP", None))
        self.Console_Players1.setText(_translate("MainWindow", "PLAYERS (1)", None))
        self.Console_Players2.setText(_translate("MainWindow", "PLAYERS (2)", None))
        self.pushButton_30.setText(_translate("MainWindow", "COMING UP\n"
"NEXT", None))
        self.Console_TweetFeed.setText(_translate("MainWindow", "TWEET FEED", None))
        self.Console_TweetSingle.setText(_translate("MainWindow", "SINGLE TWEET", None))
        self.Console_IRC.setText(_translate("MainWindow", "IRC CHAT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "CONTROL", None))
        self.label_6.setText(_translate("MainWindow", "24:30 PM UTC", None))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy HH:mm", None))
        self.label_5.setText(_translate("MainWindow", "Starting Time", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Casting Match", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Playing Game", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Review", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Interview", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "Podcast", None))
        self.label_3.setText(_translate("MainWindow", "Title", None))
        self.label_4.setText(_translate("MainWindow", "Type", None))
        self.label_7.setText(_translate("MainWindow", "Description", None))
        self.label_8.setText(_translate("MainWindow", "Image", None))
        self.pushButton_5.setText(_translate("MainWindow", "Add", None))
        self.pushButton.setText(_translate("MainWindow", "Update", None))
        self.pushButton_3.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_2.setText(_translate("MainWindow", "Import", None))
        self.pushButton_4.setText(_translate("MainWindow", "Export", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "CPH Wolves vs.  Begrip", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "0h30m", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Schedule", None))
        self.label.setText(_translate("MainWindow", "Image1", None))
        self.label_2.setText(_translate("MainWindow", "Image2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Teams", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Players", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Events", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Statistics", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Match Results", None))
        self.tweet_search_line.setText(_translate("MainWindow", "#CSGO", None))
        self.tweet_search_line.setPlaceholderText(_translate("MainWindow", "Search", None))
        self.get_tweets_btn.setText(_translate("MainWindow", "Get Tweets", None))
        self.BTN_TweetSingle.setText(_translate("MainWindow", "Show Single", None))
        self.tweetshow.setText(_translate("MainWindow", "Add", None))
        self.pushButton_33.setText(_translate("MainWindow", "Remove", None))
        self.tweet_table.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Twitter", None))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Twitch Chat", None))
        self.console_go.setText(_translate("MainWindow", "Send to Server", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionFullsreen.setText(_translate("MainWindow", "Toggle Fullscreen", None))
        self.actionFullsreen.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionImport_Scedule.setText(_translate("MainWindow", "Import Schedule", None))
        self.actionExport_Schedule.setText(_translate("MainWindow", "Export Schedule", None))
        self.actionImport_Schedule.setText(_translate("MainWindow", "Import Schedule", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionReload_Client.setText(_translate("MainWindow", "Reload Client", None))
        self.actionReload_Client.setShortcut(_translate("MainWindow", "Ctrl+R", None))

import icons_rc
