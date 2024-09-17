import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("./ui/main_window.ui", self)
        self.set_connections()
    
    def set_connections(self):
        # Connect buttons to their respective functions
        self.btn_back.clicked.connect(self.go_to_main_window)
        self.btn_back_2.clicked.connect(self.go_to_main_window)
        self.btn_back_3.clicked.connect(self.go_to_main_window)

        self.btn_chat_list.clicked.connect(self.go_to_chat_window)
        self.btn_contacts_list.clicked.connect(self.go_to_contacts_list_window)
        self.btn_new_chat.clicked.connect(self.go_to_new_chat_window)

    def go_to_chat_window(self):
        # Switch to the chat page (assuming it's at index 1 in the QStackedWidget)
        self.stackedWidget.setCurrentIndex(1)

    def go_to_main_window(self):
        # Switch back to the main page (assuming it's at index 0)
        self.stackedWidget.setCurrentIndex(0)

    def go_to_contacts_list_window(self):
        # Switch back to the main page (assuming it's at index 0)
        self.stackedWidget.setCurrentIndex(2)

    def go_to_new_chat_window(self):
        # Switch back to the main page (assuming it's at index 0)
        self.stackedWidget.setCurrentIndex(3)


# Main
app = QApplication(sys.argv)
main_window = MainWindow()

# Show the main window
main_window.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
