from PyQt5.QtWidgets import (QMainWindow)

from calculator.widgets.ui_calculator import Ui_Calculator


class CalculatorWindow(QMainWindow, Ui_Calculator):
    first_num = None
    is_typing_second_num = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons
        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_plusMinus.clicked.connect(self.unary_operation_pressed)
        self.pushButton_percent.clicked.connect(self.unary_operation_pressed)

        self.pushButton_add.clicked.connect(self.binary_operation_pressed)
        self.pushButton_subtract.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equals.clicked.connect(self.equals_pressed)
        self.pushButton_clear.clicked.connect(self.clear_pressed)

        self.pushButton_add.setCheckable(True)
        self.pushButton_subtract.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

    def digit_pressed(self):
        button = self.sender()

        if (self.pushButton_add.isChecked() or
                self.pushButton_subtract.isChecked() or
                self.pushButton_multiply.isChecked() or
                self.pushButton_divide.isChecked() or
                (not self.is_typing_second_num)):
            new_label = format(float(button.text()), '.15g')
            self.is_typing_second_num = True
        else:
            if '.' in self.label.text() and button.text() == "0":
                new_label = format(self.label.text() + "0", '.15')
            else:
                new_label = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(str(new_label))

    def decimal_pressed(self):
        self.label.setText(self.label.text() + '.')

    def unary_operation_pressed(self):
        button = self.sender()

        label_number = float(self.label.text())

        if button.text() == '+/-':
            label_number = label_number * -1
        else:
            label_number = label_number * 0.01

        new_label = format(label_number, '.15g')

        self.label.setText(str(new_label))

    def binary_operation_pressed(self):
        button = self.sender()

        self.first_num = float(self.label.text())

        button.setChecked(True)

    def equals_pressed(self):

        second_num = float(self.label.text())

        if self.pushButton_add.isChecked():
            label_num = self.first_num + second_num
            self.pushButton_add.setChecked(False)
            self.label.setText(format(label_num, '.15g'))
        elif self.pushButton_subtract.isChecked():
            label_num = self.first_num - second_num
            self.pushButton_subtract.setChecked(False)
            self.label.setText(format(label_num, '.15g'))
        elif self.pushButton_multiply.isChecked():
            label_num = self.first_num * second_num
            self.pushButton_multiply.setChecked(False)
            self.label.setText(format(label_num, '.15g'))
        elif self.pushButton_divide.isChecked():
            if second_num == 0:
                self.label.setText("NaN")
            else:
                label_num = self.first_num / second_num
                self.pushButton_divide.setChecked(False)
                self.label.setText(format(label_num, '.15g'))

        self.is_typing_second_num = False

    def clear_pressed(self):
        self.label.setText('0')
        self.pushButton_add.setChecked(False)
        self.pushButton_subtract.setChecked(False)
        self.pushButton_multiply.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.is_typing_second_num = False
