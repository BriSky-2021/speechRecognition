# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from system_command import event_operation
import time
import qtawesome as qta

class Ui_MainWindow(object):


    def tips_info(self,text,color=None):
        if color!=None:
            self.label_5.setStyleSheet(color)
        self.label_5.setText(text)

    def click_button(self):
        self.tips_info("正在倾听中",'color: rgb(0, 210, 220);')
        my_event=event_operation()
        status=None
        status=my_event.push_button()
        if(status==1):
            self.tips_info("没有听清楚请重新说话",'color: rgb(117, 0, 210);')
        if (status == 0):
            self.tips_info("命令执行完毕", 'color: rgb(117, 210, 0);')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(314, 462)
        MainWindow.resize(314, 662)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 250, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(70, 50, 161, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 330, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(60, 400, 201, 51))
        self.button1.setText("Hi! Click Me")
        self.button1.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.button1.clicked.connect(self.click_button)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 465, 201, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")

        # # Styling icons
        # styling_icon = qta.icon('fa5s.music',
        #                         color='blue',
        #                         color_active='orange')
        # self.music_button = QtWidgets.QPushButton(styling_icon, 'Styling')
        # self.music_button.setText('look at me!')
        # self.music_button.setFont(font)
        # self.music_button.setGeometry(QtCore.QRect(60, 500, 201, 21))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))

