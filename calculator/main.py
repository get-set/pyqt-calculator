import sys

from PyQt5.QtWidgets import QApplication

from calculator.calc_window import CalculatorWindow

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())
