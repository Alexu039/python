# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore
from myDesigner import Ui_Dialog
import sys

# method1:
# if __name__ == "__main__":
#    app = QtWidgets.QApplication(sys.argv)
#    widget = QtWidgets.QWidget()
#    new = Ui_Dialog()
#    new.setupUi(widget)
#    widget.show()
#    sys.exit(app.exec_())

# method2:
# class myDesignershow(QtWidgets.QWidget):
#     def __init__(self):
#         super(myDesignershow,self).__init__()
#         self.new = Ui_Dialog()
#         self.new.setupUi(self)
        
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     myshow = myDesignershow()
#     myshow.show()
#     sys.exit(app.exec_())

# method3:
class myDesignershow(QtWidgets.QWidget,Ui_Dialog):
    _signal = QtCore.pyqtSignal(str) # 定义信号，指定参数为str型
    def __init__(self):
        super(myDesignershow,self).__init__()
        self.setupUi(self)
        self.pushButton1.clicked.connect(self.prn)#binding method to button
        self.pushButton2.clicked.connect(self.close)#binding method to button
        self._signal.connect(self.mysignalslot)
    
    def prn(self):
        print("test")
        self._signal.emit("slot")
    
    def mysignalslot(self,parameter):
        print(parameter)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = myDesignershow()
    myshow.show()
    sys.exit(app.exec_())
\ No newline at end of file
