import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        loadUi("./ui/main_window.ui", self)
        self.set_connections()
    
    def set_connections(self):
        # Button
        self.btn_chat_list.clicked.connect(self.go_to_chat_window)
        # self.connect_button.clicked.connect(self.button_clicked)

    def go_to_chat_window(self):
        # Switch to the second window (index 1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def button_clicked(self):
        print('click!')

class ChatWindow(QDialog):
    def __init__(self):
        super(ChatWindow, self).__init__()
        loadUi("./ui/chat_list.ui", self)
        self.set_connections()
    
    def set_connections(self):
        # Example: Connect a button in the chat window to switch back to the main window
        self.btn_back.clicked.connect(self.go_to_main_window)

    def go_to_main_window(self):
        # Switch back to the main window (index 0)
        widget.setCurrentIndex(widget.currentIndex() - 1)

# Main
app = QApplication(sys.argv)
main_window = MainWindow()
# chat_window = ChatWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
# widget.addWidget(chat_window)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")