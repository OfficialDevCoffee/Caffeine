# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_chatandpeople = QtWidgets.QHBoxLayout()
        self.horizontalLayout_chatandpeople.setObjectName("horizontalLayout_chatandpeople")
        self.verticalLayout_chat = QtWidgets.QVBoxLayout()
        self.verticalLayout_chat.setObjectName("verticalLayout_chat")
        self.listWidget_chat = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_chat.setAutoScroll(True)
        self.listWidget_chat.setWordWrap(True)
        self.listWidget_chat.setObjectName("listWidget_chat")
        self.verticalLayout_chat.addWidget(self.listWidget_chat)
        self.verticalLayout_chat.setStretch(0, 4)
        self.horizontalLayout_chatandpeople.addLayout(self.verticalLayout_chat)
        self.verticalLayout_people = QtWidgets.QVBoxLayout()
        self.verticalLayout_people.setObjectName("verticalLayout_people")
        self.label_people = QtWidgets.QLabel(self.centralwidget)
        self.label_people.setAlignment(QtCore.Qt.AlignCenter)
        self.label_people.setObjectName("label_people")
        self.verticalLayout_people.addWidget(self.label_people)
        self.listWidget_people = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_people.setWordWrap(True)
        self.listWidget_people.setObjectName("listWidget_people")
        self.verticalLayout_people.addWidget(self.listWidget_people)
        self.horizontalLayout_chatandpeople.addLayout(self.verticalLayout_people)
        self.horizontalLayout_chatandpeople.setStretch(0, 4)
        self.horizontalLayout_chatandpeople.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_chatandpeople)
        self.horizontalLayout_send = QtWidgets.QHBoxLayout()
        self.horizontalLayout_send.setObjectName("horizontalLayout_send")
        self.textEdit_send = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_send.sizePolicy().hasHeightForWidth())
        self.textEdit_send.setSizePolicy(sizePolicy)
        self.textEdit_send.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_send.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_send.setObjectName("textEdit_send")
        self.horizontalLayout_send.addWidget(self.textEdit_send)
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_send.addWidget(self.pushButton_send)
        self.horizontalLayout_send.setStretch(0, 9)
        self.horizontalLayout_send.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_send)
        self.verticalLayout_3.setStretch(0, 9)
        self.verticalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 18))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuRoom = QtWidgets.QMenu(self.menubar)
        self.menuRoom.setObjectName("menuRoom")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect_to_Server = QtWidgets.QAction(MainWindow)
        self.actionConnect_to_Server.setObjectName("actionConnect_to_Server")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.menuConnection.addAction(self.actionConnect_to_Server)
        self.menuConnection.addAction(self.actionDisconnect)
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuRoom.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caffeine"))
        self.label_people.setText(_translate("MainWindow", "People"))
        self.listWidget_people.setSortingEnabled(True)
        self.pushButton_send.setText(_translate("MainWindow", "Send"))
        self.menuConnection.setTitle(_translate("MainWindow", "Connect"))
        self.menuRoom.setTitle(_translate("MainWindow", "Room"))
        self.actionConnect_to_Server.setText(_translate("MainWindow", "Connect to Server"))
        self.actionConnect_to_Server.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionDisconnect.setShortcut(_translate("MainWindow", "Ctrl+2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
