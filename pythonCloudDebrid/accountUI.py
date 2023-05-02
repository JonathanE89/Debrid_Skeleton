from userData import UserData
import sys, re
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QPushButton, QSplitter, QFrame, QScrollArea, QLayout, QTextBrowser, QLineEdit, QMessageBox
from PySide6.QtCore import QTimer

#Initialize UserData in Accounts Form 
#NOTE: MISSING AccountSettings for Security Features
activeUser = UserData()

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
        button_1 = QPushButton("Sign Up")
        button_layout.addWidget(button_1)
        button_1.clicked.connect(self.register_user)

        # Add spacer item to evenly distribute buttons
        #button_layout.addStretch()

        # Add button 2
        #button_2 = QPushButton("Button 2")
        #button_layout.addWidget(button_2)

        # Add button layout to main layout
        layout.addLayout(button_layout)

        # Set the layout for the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    #Allows the User to Register an Account
    def register_user(self):
        username = self.username_box.text()
        password = self.password_box.text()
        confirm_password = self.confirm_password_box.text()
        email = self.email_box.text()

        email_pattern = re.compile(r'^[\w.-]+@[\w.-]+\.\w+$')
        username_password_pattern = re.compile(r'^(?![-.])[a-zA-Z0-9!()\-._?[\]{}`~;:#!$%&*+=]+$')

        if username and password and (password == confirm_password):
            if email_pattern.match(email) and username_password_pattern.match(username) and username_password_pattern.match(password):
                # Check for existing email and username in users.dat file
                with open('pythonCloudDebrid/acc/users.dat', 'r') as f:
                    user_data = f.readlines()

                for line in user_data:
                    existing_email, existing_username, _ = line.strip().split(' || ')
                    existing_email = existing_email[4:]
                    existing_username = existing_username.strip()
                    if email == existing_email:
                        QMessageBox.warning(self, "Error", "That Email is already in use. Please choose a different one.")
                        return
                    elif username == existing_username:
                        QMessageBox.warning(self, "Error", "That Username is already in use. Please choose a different one.")
                        return

                # Save user info to users.dat file if email and username are unique
                with open('pythonCloudDebrid/acc/users.dat', 'a') as f:
                    f.write(f"\n{email} || {username} || {password}")
                self.close()
            else:
                # Show an error message if the email, username, or password is invalid
                QMessageBox.warning(self, "Error", "Invalid email, username, or password. Please ensure they are in the correct format and contain allowed characters.")
        else:
            # Show an error message if the registration data is invalid
            QMessageBox.warning(self, "Error", "Please make sure all fields are filled, and the passwords match.")


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
        button_1.clicked.connect(self.loginUser)

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
    
    #Allows the User to Log-In (store active user data)
    def loginUser(self):
        username = self.username_box.text()
        password = self.password_box.text()
        with open('pythonCloudDebrid/acc/users.dat', 'r') as f:
            user_data = f.readlines()

        for line in user_data:
            # Skip blank lines
            if not line.strip():
                continue

            existing_email, existing_username, existing_password = line.strip().split(' || ')
            if username == existing_username and password == existing_password:
                # Set the activeUser with the logged-in user's information
                activeUser.log_in(username, password)
                print("Successfully Logged In!")
                self.close()  # Close the window on successful login
                return True

        # If the loop completes without finding a match, show an error message
        QMessageBox.warning(self, "Error", "Invalid username or password. Please try again.")
        return False


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
        self.login_button = QPushButton("Log In")
        button_layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.show_login_window)

        # Add button 1 (Log Out)
        self.logout_button = QPushButton("Log Out")
        button_layout.addWidget(self.logout_button)
        self.logout_button.clicked.connect(self.logoutUser)
        self.logout_button.hide()

        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 2 (Sign Up)
        self.register_button = QPushButton("Sign Up")
        button_layout.addWidget(self.register_button)
        self.register_button.clicked.connect(self.show_register_window)
        
        # Add button layout to main layout
        layout.addLayout(button_layout)

        # Set the layout for the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Set up QTimer to update username_box every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_username_box)
        self.timer.timeout.connect(self.update_login_button)
        self.timer.start(1000)

    #Allows the User to Log-Out (remove active user data)
    def logoutUser(self):
        activeUser.log_out()

    def update_username_box(self):
        self.username_box.setText(activeUser.showUser())

    def show_login_window(self):
        self.login_window.show()

    def show_register_window(self):
        self.register_window.show()

    def update_login_button(self):
        if self.username_box.text() == "No User Detected":
            self.login_button.show()
            self.logout_button.hide()
        else:
            self.login_button.hide()
            self.logout_button.show()

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

