# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 463)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 400, 221, 51))
        self.pushButton.setStyleSheet("color: rgb(85, 255, 255);\n"
"background-color: rgb(85, 85, 127);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 90, 571, 51))
        self.label.setStyleSheet("background-color: rgb(117, 114, 99);\n"
"color: rgb(255, 255, 102);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(1)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 9, 361, 71))
        self.lineEdit.setStyleSheet("color: rgb(85, 255, 255);\n"
"border-color: rgb(0, 85, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 85, 127);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 571, 51))
        self.label_2.setStyleSheet("background-color: rgb(117, 114, 99);\n"
"color: rgb(255, 255, 102);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(5)
        self.label_2.setMidLineWidth(1)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 571, 51))
        self.label_3.setStyleSheet("background-color: rgb(117, 114, 99);\n"
"color: rgb(255, 255, 102);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(5)
        self.label_3.setMidLineWidth(1)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 571, 51))
        self.label_4.setStyleSheet("background-color: rgb(117, 114, 99);\n"
"color: rgb(255, 255, 102);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(5)
        self.label_4.setMidLineWidth(1)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 330, 571, 51))
        self.label_5.setStyleSheet("background-color: rgb(117, 114, 99);\n"
"color: rgb(255, 255, 102);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setLineWidth(5)
        self.label_5.setMidLineWidth(1)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Получить"))
