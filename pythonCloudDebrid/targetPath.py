import os

#Creates a Target Path (Singleton)
class TargetPath:
    _instance = None
    _path = ""

    #There is only One Target Path at a time.
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TargetPath, cls).__new__(cls)
        return cls._instance

    #Gets Target Path 
    def get_path(self):
        return self._path

    #Sets Target Path
    def set_path(self, url):
        self._path = url

    #Ensures Target Path is Valid
    def assert_path(self):
        if not os.path.exists(self._path):
            print("The path does not exist.")
            return False
        if not os.path.isabs(self._path):
            print("The path is not an absolute path.")
            return False
        return True

'''
# Example usage
if __name__ == "__main__":
    target_path = TargetPath()
    target_path.set_path("/some/absolute/path")
    print("Path:", target_path.get_path())
    print("Is the path valid?", target_path.assert_path())'''
