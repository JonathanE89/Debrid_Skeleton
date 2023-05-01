import accountUI
from accountUI import launch_AccountWindow
import re, os, subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QSizePolicy, QLabel, QHBoxLayout, QPushButton, QSplitter, QFrame, QScrollArea, QLayout, QTextBrowser
from PySide6.QtCore import QTimer

#method that uses regular expressions to find all the URLs in a text and return them as an array
def find_urls(text):
    urls = []
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    for url in re.findall(pattern, text):
        urls.append(url)
    return urls

#method that runs the main window
class DebridWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Debrid")
        self.setFixedSize(self.size())
        layout = QVBoxLayout()

        # Add a text box
        self.text_box = QTextEdit()
        self.text_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.text_box, 1)

        # Add a content_box
        self.content_box = QVBoxLayout()
        self.content_box.setContentsMargins(0, 0, 0, 0)
        self.content_box.setSpacing(0)
        
        # Adds a place for text in the content_box
        self.content_label = QTextBrowser()
        self.content_label.setOpenExternalLinks(True)
        self.content_box.addWidget(self.content_label)

        # Add the content_box to a scrollable area
        scroll_content = QWidget()
        scroll_content.setStyleSheet("border: 1px solid #444444")
        scroll_content.setLayout(self.content_box)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(scroll_content)

        # Add the scrollable area to the main layout
        layout.addWidget(scroll, 3)


        # Add horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)

        # Add button 1
        button_1 = QPushButton("Accounts")
        button_layout.addWidget(button_1)
        button_1.clicked.connect(launch_AccountWindow)

        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 2
        button_2 = QPushButton("Button 2")
        button_layout.addWidget(button_2)

        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 3
        button_3 = QPushButton("Button 3")
        button_layout.addWidget(button_3)

        # Add horizontal frame separator between link_box and buttons
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Add button layout to main layout
        layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Create timer object
        self.timer = QTimer(self)
        
        # Connect timer to parseText method
        self.timer.timeout.connect(self.parseText)
        
        # Start timer with 1000 ms interval (1 second)
        self.timer.start(1000)
    
    #Method to Parse Text for the Debrid
    def parseText(self):
            # Get the text from the text_box
            input_text = self.text_box.toPlainText()
            parsed_text = find_urls(input_text)

            # Testing Input
            #print(parsed_text)
            
            # Add the text to the content_box using a QLabel
            parsed_urls = ''.join(f'<p><a href="{url}">{url}</a></p>' for url in parsed_text)
            self.content_label.setHtml(parsed_urls)
        
    #method that calls the accountUI.py function
    def run_accounts(self):
        script_path = os.path.join("pythonCloudDebrid", "accountUI.py")
        subprocess.run(["python", script_path])    

if __name__ == "__main__":
    app = QApplication([])
    window = DebridWindow()
    window.show()
    app.exec()
