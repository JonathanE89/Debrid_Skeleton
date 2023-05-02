#Establishes the Active User (Singleton)
class UserData:
    _instance = None

    #Only One User Exists at a Time.
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logged_in = False
            cls._instance.username = None
            cls._instance.password = None
        return cls._instance

    #Method to Establish an Active User
    def log_in(self, username, password):
        self.logged_in = True
        self.username = username
        self.password = password

    #Method to Remove an Active User
    def log_out(self):
        self.logged_in = False
        self.username = None
        self.password = None
        
    # Method to show the username of the logged-in user
    def showUser(self):
        if self.logged_in:
            return self.username
        else:
            return "No User Detected"