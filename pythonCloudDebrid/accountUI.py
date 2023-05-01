import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QPushButton, QSplitter, QFrame, QScrollArea, QLayout, QTextBrowser, QLineEdit
from PySide6.QtCore import QTimer

#Register Window for Accounts User Interface
class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account: Register")
        window_width = 400
        window_height = 300
        self.setFixedSize(window_width, window_height)
        layout = QVBoxLayout()
        
        # Establish Layout of User Info
        info_layout = QVBoxLayout()
        info_layout.setSpacing(1)
        info_layout.setContentsMargins(0, 0, 0, 10)

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

        # Add a label for the confirm password
        self.confirm_password_label = QLabel("Confirm Password:")
        info_layout.addWidget(self.confirm_password_label)

        # Add a text box for the confirm password
        self.confirm_password_box = QLineEdit()
        self.confirm_password_box.setEchoMode(QLineEdit.EchoMode.Password)
        info_layout.addWidget(self.confirm_password_box)

        # Add a label for the e-mail
        self.email_label = QLabel("E-Mail:")
        info_layout.addWidget(self.email_label)

        # Add a text box for the e-mail
        self.email_box = QLineEdit()
        info_layout.addWidget(self.email_box)

        # Incorporates the info_layout into the main layout
        layout.addLayout(info_layout)

        # Add horizontal frame separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Establish Layout for Buttons
        button_layout = QHBoxLayout()

        # Add button 1
        button_1 = QPushButton("Button 1")
        button_layout.addWidget(button_1)

        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 2
        button_2 = QPushButton("Button 2")
        button_layout.addWidget(button_2)

        # Add button layout to main layout
        layout.addLayout(button_layout)

        # Set the layout for the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

#Login Window for Account User Interface
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account: Log In")
        window_width = 400
        window_height = 200
        self.setFixedSize(window_width, window_height)
        layout = QVBoxLayout()
        
        # Create an instance of RegisterWindow
        self.register_window = RegisterWindow()
        
        #Method to show the RegisterWindow
        def show_register_window():
            self.register_window.show() 
                          
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
        button_2.clicked.connect(show_register_window)
         
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

class AccountWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account")
        window_width = 400
        window_height = 200
        self.setFixedSize(window_width, window_height)
        layout = QVBoxLayout()
        
        # Create instances of LoginWindow and RegisterWindow
        self.login_window = LoginWindow()
        self.register_window = RegisterWindow()

        # Establish Layout of User Info
        info_layout = QVBoxLayout()
        info_layout.setSpacing(1)
        info_layout.setContentsMargins(0, 0, 0, 10)

        # Add a label for the username
        self.username_label = QLabel("Username:")
        info_layout.addWidget(self.username_label)

        # Add a text box for the username
        self.username_box = QLineEdit("No User Detected")
        self.username_box.setReadOnly(True)
        info_layout.addWidget(self.username_box)

        # Add a label for the password
        #self.password_label = QLabel("Password:")
        #info_layout.addWidget(self.password_label)

        # Add a text box for the password
        #self.password_box = QLineEdit("No User Detected")
        #self.password_box.setEchoMode(QLineEdit.EchoMode.Password)
        #self.password_box.setReadOnly(True)
        #info_layout.addWidget(self.password_box)

        # Incorporates the info_layout into the main layout
        layout.addLayout(info_layout)

        # Add horizontal frame separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Establish Layout for Buttons
        button_layout = QHBoxLayout()

        # Add button 1 (Log In)
        button_1 = QPushButton("Log In")
        button_layout.addWidget(button_1)
        button_1.clicked.connect(self.show_login_window)

        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 2 (Sign Up)
        button_2 = QPushButton("Sign Up")
        button_layout.addWidget(button_2)
        button_2.clicked.connect(self.show_register_window)

        # Add button layout to main layout
        layout.addLayout(button_layout)

        # Set the layout for the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_login_window(self):
        self.login_window.show()

    def show_register_window(self):
        self.register_window.show()


#Launch Windows
'''
def launch_windows():
    app = QApplication([])

    # Show Login Window
    login_window = LoginWindow()
    login_window.show()

    # Show Register Window
    register_window = RegisterWindow()
    register_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    launch_windows()
'''

#Test First Window
def launch_AccountWindow(app):      
    #if __name__ == "__main__":
        #app = QApplication([])
        window = AccountWindow()
        window.show()
        app.exec()

#Actual Executed Code 
#launch_AccountWindow()

