# Cloud Debrid
- Last Updated: May 1st, 2023
    
# NOTE:
there is currently **no release version** of Cloud Debrid available. All methods of operating this software requires running it in the terminal manually. 

# How To Use:
## Dependencies Required:
- Python 3
- PySide6 
- BeautifulSoup
- All Files in this Repository

## Running The Software:
- To operate Cloud Debrid in it's current state, you need to manually run the debridUI.py script, which is then used to navigate the other components. 

## Navigating The Software: 
### **Debrid:** 
- Debrid is a window where you can insert text, and from that text, parse direct download links found in the urls of that text. Users can opt to either click specific direct-download hyperlinks, or download all available files to a set Target Path on their computer. Currently, the debrid supports the following websites:
    - https://archive.org/ 
    - https://drive.google.com/
### **Accounts:** 
- Accounts is a window where you can register, log in, and log out users. This method is currently only functional on a local level, and accounts are not stored in any database other than the `users.dat` file.

# Future Features:
### **Database Support:** 
- In the future, there will be database support for Account and File Storage Features. This will allow users to set their Target Path to a cloud database that they can use to browse and download specific files. 
### **Account Security:** 
- Since account information is stored locally, there are currently no protections for storing account information. In the future, the junction of database support will include methods to encrypt and decrypt user data to ensure account integrity and security. 
### **Modularity:** 
- Currently, code is compact in order to guarantee the functionality of the core processes in Cloud Debrid. As the code is expanded on, classes and methods will recieve more modular design to ultimately save time bugfixing and writing code. This will include separate back-end classes and methods for specifically account and database-oriented methods. 
### **Debrid Compatibility:** 
- The current back-end debrid implementation is modular to easily accomodate the analysis of different types of links. Currently, it is only functional for a limited set of websites to ensure that the system works correctly and efficiently. Over the course of Cloud Debrid's development, the availablility of websites will be expanded upon to accomodate diferent websites and file-types. For a comprehensive list of acceptable websites, read the **Debrid** section of **Navigating The Software** above. 

# Known Bugs:
- When users insert direct download links into the Debrid Text Box, the main Debrid window will crash. To avoid this, only insert links that have download links available on them, instead of inserting the download links directly. 

# Credits:

### Associated Members:
- Amelia Rotondo
- Jonathan Escobedo
- George Ruiz
- Omar Trejo
- Hongfei Wang  
