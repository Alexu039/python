# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        # create Form named as "Dialog"
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 320)

        # define label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label.setObjectName("label")

        # define text
        self.num1 = QtWidgets.QTextEdit(Dialog)
        self.num1.setGeometry(QtCore.QRect(80, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")

        # define button1
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(70, 100, 75, 23))
        self.pushButton1.setObjectName("pushButton1")

        # define button2
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(70, 140, 75, 23))
        self.pushButton2.setObjectName("pushButton2")

        # set prompt
        self.retranslateUi(Dialog)

        # binding method to button
#        self.pushButton1.clicked.connect(self.prn)#binding method to button
#        self.pushButton2.clicked.connect(Dialog.close)#binding method to button

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # set window title
        Dialog.setWindowTitle(_translate("Dialog", "MyWindow"))
        # set label prompt
        self.label.setText(_translate("Dialog", "Number1:"))

        # set button prompt
        self.pushButton1.setText(_translate("Dialog", "打印"))
        self.pushButton2.setText(_translate("Dialog", "关闭窗口"))

#    def prn(self):
#        print("test")
        
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    widget = QtWidgets.QWidget()
#    ui = Ui_Dialog()
#    ui.setupUi(widget)
#    widget.show()
#    sys.exit(app.exec_())

