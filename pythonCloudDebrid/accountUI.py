from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QPushButton, QSplitter, QFrame, QScrollArea, QLayout, QTextBrowser
from PySide6.QtCore import QTimer

class AccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account")
        self.setFixedSize(self.size())
        layout = QVBoxLayout()

        # Add a text box
        self.text_box = QTextEdit()
        self.text_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.text_box, 1)

        
if __name__ == "__main__":
    app = QApplication([])
    window = AccountWindow()
    window.show()
    app.exec()  