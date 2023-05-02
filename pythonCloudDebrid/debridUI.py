import debrid
from accountUI import launch_AccountWindow

import os, requests
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QSizePolicy, QHBoxLayout, QPushButton, QFrame, QScrollArea, QTextBrowser, QFileDialog
from PySide6.QtCore import QTimer, QThread

#Creates an Instance to Find Download Links
debrid = debrid.Debrid()

#method that runs the main window
class DebridWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Debrid")
        window_width = 500
        window_height = 400
        self.setFixedSize(window_width, window_height)
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
        button_2 = QPushButton("Set Path")
        button_layout.addWidget(button_2)
        button_2.clicked.connect(self.select_target_path)
        
        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 4
        button_3 = QPushButton("Download to Path")
        button_layout.addWidget(button_3)
        button_3.clicked.connect(self.download_to_path)
        
        # Add spacer item to evenly distribute buttons
        button_layout.addStretch()

        # Add button 4
        button_4 = QPushButton("Database")
        button_layout.addWidget(button_4)

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
        
        # Connect timer to parse_text method
        self.timer.timeout.connect(self.parse_text)
        
        # Start timer with 1000 ms interval (1 second)
        self.timer.start(1000)
    
    #Method to Parse Text for the Debrid
    def parse_text(self):
            # Get the text from the text_box
            input_text = self.text_box.toPlainText()
            parsed_text = debrid.find_all_downloads(input_text)

            # Testing Input
            #print(parsed_text)
            
            # Add the text to the content_box using a QLabel
            parsed_urls = ''.join(f'<p><a href="{url}">{url}</a></p>' for url in parsed_text)
            self.content_label.setHtml(parsed_urls)
    
    #Method to Select a Target File    
    def select_target_path(self):
        target_directory = QFileDialog.getExistingDirectory(self, "Select Target Directory")
        if target_directory:
            debrid.set_download_path(target_directory)
            print(f"Target path set to: {target_directory}")
        else:
            print("No directory selected")
    
    # Method to download files to the specified target path
    def download_to_path(self):
        print("Trying to Download to Path")
        input_text = self.text_box.toPlainText()
        download_links = debrid.find_all_downloads(input_text)
        print(f"Download Links Found: {download_links}")

        target_path = debrid.activePath.get_path()
        if not target_path:
            print("No target path specified")
            return

        self.downloader = Downloader(download_links, target_path)  # Create a Downloader instance
        self.downloader.start()  # Start the worker thread

    '''#OLD method that calls the accountUI.py function
        def runAccounts(self):
            # OUTDATED & UNNECESSARY # 
            script_path = os.path.join("pythonCloudDebrid", "accountUI.py")
            subprocess.run(["python", script_path])'''    

#Helper Class for Managing Downloads
class Downloader(QThread):
    def __init__(self, urls, target_path):
        super().__init__()
        self.urls = urls
        self.target_path = target_path

    #Integrates download_single_file to smoothen downloads
    def run(self):
        for url in self.urls:
            try:
                local_filename = self.download_single_file(url)
                print(f"Downloaded {local_filename} to {self.target_path}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")

    #Downloads a Single File from a URL
    def download_single_file(self, url):
        local_filename = url.split('/')[-1]
        target_path = os.path.join(self.target_path, local_filename)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(target_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        return local_filename


if __name__ == "__main__":
    app = QApplication([])
    window = DebridWindow()
    window.show()
    app.exec()
