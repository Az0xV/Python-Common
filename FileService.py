"""
Example use:
file = FileService("name.txt") # This creates a new object of FileService class
file.writeFile("Example file data to write") # This creates a file and writes the data into it
file.appendFile("/nExample file data to append") # This method appends to already existing file (with break line at the beginning)
fileData = file.readFile() # This function will read the file, and save it in the fileData variable.
print(fileData) # output:
# Example file data to write
# Example file data to append

The example above shows what this tool can do.
"""

class FileService:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = None
    
    def readFile(self):
        try:
            fileObject = open(self.fileName, "r")
        except FileNotFoundError:
            return None
        data = fileObject.read()
        fileObject.close()
        self.data = data
        return self.data
    
    def writeFile(self, data):
        fileObject = open(self.fileName, "w")
        fileObject.write(data)
        fileObject.close()
    
    def appendFile(self, data):
        fileObject = open(self.fileName, "a")
        fileObject.write(data)
        fileObject.close()
