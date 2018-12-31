# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(241, 361)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"background-color: white;")
        self.label.setObjectName("label")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215,215,215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_plusMinus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plusMinus.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.pushButton_plusMinus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215,215,215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(120, 60, 61, 61))
        self.pushButton_percent.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215,215,215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(180, 60, 61, 61))
        self.pushButton_divide.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255,151,57);\n"
"  color: white;\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff7832, stop: 1 #ff9739);\n"
"}")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255,151,57);\n"
"  color: white;\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff7832, stop: 1 #ff9739);\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_subtract.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.pushButton_subtract.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255,151,57);\n"
"  color: white;\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff7832, stop: 1 #ff9739);\n"
"}")
        self.pushButton_subtract.setObjectName("pushButton_subtract")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255,151,57);\n"
"  color: white;\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff7832, stop: 1 #ff9739);\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 300, 121, 61))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.pushButton_decimal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215,215,215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bebebe, stop: 1 #d7d7d7);\n"
"}")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.pushButton_equals.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255,151,57);\n"
"  color: white;\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #ff7832, stop: 1 #ff9739);\n"
"}")
        self.pushButton_equals.setObjectName("pushButton_equals")
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.label.setText(_translate("Calculator", "0"))
        self.pushButton_clear.setText(_translate("Calculator", "C"))
        self.pushButton_plusMinus.setText(_translate("Calculator", "+/-"))
        self.pushButton_percent.setText(_translate("Calculator", "%"))
        self.pushButton_divide.setText(_translate("Calculator", "÷"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_multiply.setText(_translate("Calculator", "x"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_subtract.setText(_translate("Calculator", "-"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_add.setText(_translate("Calculator", "+"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_decimal.setText(_translate("Calculator", "."))
        self.pushButton_equals.setText(_translate("Calculator", "="))

