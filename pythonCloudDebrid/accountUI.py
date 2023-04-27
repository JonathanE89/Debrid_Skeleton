from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QPushButton, QSplitter, QFrame, QScrollArea, QLayout, QTextBrowser, QLineEdit
from PySide6.QtCore import QTimer

class AccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account")
        window_width = 400
        window_height = 200
        self.setFixedSize(window_width, window_height)
        layout = QVBoxLayout()
                
        #Establish Layout of User Info
        info_layout = QVBoxLayout()
        info_layout.setSpacing(1)
        info_layout.setContentsMargins(0,0,0,10)

        # Add a label for the username
        self.username_label = QLabel("Username:")
        info_layout.addWidget(self.username_label)

        # Add a text box for the username
        self.username_box = QLineEdit()
        info_layout.addWidget(self.username_box)

        # Add a label for the password
        self.password_label = QLabel("Password:")
        info_layout.addWidget(self.password_label)

        # Add a text box for the password
        self.password_box = QLineEdit()
        self.password_box.setEchoMode(QLineEdit.EchoMode.Password)
        info_layout.addWidget(self.password_box)
        
        #Incorporates the info_layout into the main layout
        layout.addLayout(info_layout)
        
        # Add horizontal frame separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Establish Layout for Buttons
        button_layout = QHBoxLayout()

        # Add button 1
        button_1 = QPushButton("Log In")
        button_layout.addWidget(button_1)

        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 2
        button_2 = QPushButton("Sign Up")
        button_layout.addWidget(button_2)

        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 3
        button_3 = QPushButton("Forgot Password")
        button_layout.addWidget(button_3)

        # Add button layout to main layout
        layout.addLayout(button_layout)
        
        # Set the layout for the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        
if __name__ == "__main__":
    app = QApplication([])
    window = AccountWindow()
    window.show()
    app.exec()  