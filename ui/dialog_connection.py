# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_connection.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Connection(object):
    def setupUi(self, Dialog_Connection):
        Dialog_Connection.setObjectName("Dialog_Connection")
        Dialog_Connection.resize(360, 150)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Connection)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_host = QtWidgets.QHBoxLayout()
        self.horizontalLayout_host.setObjectName("horizontalLayout_host")
        self.label_host = QtWidgets.QLabel(Dialog_Connection)
        self.label_host.setAlignment(QtCore.Qt.AlignCenter)
        self.label_host.setObjectName("label_host")
        self.horizontalLayout_host.addWidget(self.label_host)
        self.plainTextEdit_host = QtWidgets.QPlainTextEdit(Dialog_Connection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_host.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_host.setSizePolicy(sizePolicy)
        self.plainTextEdit_host.setToolTip("")
        self.plainTextEdit_host.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_host.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_host.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit_host.setObjectName("plainTextEdit_host")
        self.horizontalLayout_host.addWidget(self.plainTextEdit_host)
        self.horizontalLayout_host.setStretch(0, 1)
        self.horizontalLayout_host.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_host)
        self.horizontalLayout_port = QtWidgets.QHBoxLayout()
        self.horizontalLayout_port.setObjectName("horizontalLayout_port")
        self.label_port = QtWidgets.QLabel(Dialog_Connection)
        self.label_port.setAlignment(QtCore.Qt.AlignCenter)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_port.addWidget(self.label_port)
        self.plainTextEdit_port = QtWidgets.QPlainTextEdit(Dialog_Connection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_port.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_port.setSizePolicy(sizePolicy)
        self.plainTextEdit_port.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_port.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_port.setObjectName("plainTextEdit_port")
        self.horizontalLayout_port.addWidget(self.plainTextEdit_port)
        self.horizontalLayout_port.setStretch(0, 1)
        self.horizontalLayout_port.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_port)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_Connection)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(Dialog_Connection)
        self.buttonBox.accepted.connect(Dialog_Connection.accept)
        self.buttonBox.rejected.connect(Dialog_Connection.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Connection)

    def retranslateUi(self, Dialog_Connection):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Connection.setWindowTitle(_translate("Dialog_Connection", "Dialog"))
        self.label_host.setText(_translate("Dialog_Connection", "HOST"))
        self.label_port.setText(_translate("Dialog_Connection", "PORT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Connection = QtWidgets.QDialog()
    ui = Ui_Dialog_Connection()
    ui.setupUi(Dialog_Connection)
    Dialog_Connection.show()
    sys.exit(app.exec_())
