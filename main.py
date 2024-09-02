import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        loadUi("./ui/main_window.ui", self)

        # Button
        # self.button.clicked.connect(self.button_clicked)

        def button_clicked(self):
            print()

# Main
app = QApplication(sys.argv)
main_window = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")