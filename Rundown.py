# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addrundown.ui'
#
# Created: Tue Aug 27 00:44:04 2013
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

class Ui_Rundown(object):
    def setupUi(self, Rundown):
        Rundown.setObjectName(_fromUtf8("Rundown"))
        Rundown.resize(483, 272)
        Rundown.setStyleSheet(_fromUtf8("/*\n"
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
        self.verticalLayout = QtGui.QVBoxLayout(Rundown)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Rundown)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.event = QtGui.QComboBox(self.widget)
        self.event.setObjectName(_fromUtf8("event"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.event)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.team1 = QtGui.QComboBox(self.widget)
        self.team1.setObjectName(_fromUtf8("team1"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.team1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.team2 = QtGui.QComboBox(self.widget)
        self.team2.setObjectName(_fromUtf8("team2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.team2)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.game = QtGui.QComboBox(self.widget)
        self.game.setObjectName(_fromUtf8("game"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.game)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.start = QtGui.QDateTimeEdit(self.widget)
        self.start.setCalendarPopup(False)
        self.start.setObjectName(_fromUtf8("start"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.start)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.title = QtGui.QLineEdit(self.widget)
        self.title.setObjectName(_fromUtf8("title"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.title)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtGui.QDialogButtonBox(Rundown)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Rundown)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Rundown.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Rundown.reject)
        QtCore.QMetaObject.connectSlotsByName(Rundown)

    def retranslateUi(self, Rundown):
        Rundown.setWindowTitle(_translate("Rundown", "Rundown", None))
        self.label.setText(_translate("Rundown", "Event", None))
        self.label_3.setText(_translate("Rundown", "Team 1", None))
        self.label_2.setText(_translate("Rundown", "Team 2", None))
        self.label_4.setText(_translate("Rundown", "Game", None))
        self.label_5.setText(_translate("Rundown", "Start Time", None))
        self.start.setDisplayFormat(_translate("Rundown", "dd/MM/yyyy HH:mm", None))
        self.label_6.setText(_translate("Rundown", "Title", None))

import icons_rc
