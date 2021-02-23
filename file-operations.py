#Files - opening and reading a file in the same directory/folder
myfile = open("routers.txt", "r") #"r" is the file access mode for reading and it is the default mode when opening a file

#Files - opening and reading a file in another directory/folder on Windows
myfile = open("C:\\Users\\john\\routers.txt", "r") #"r" is the file access mode for reading and it is the default mode when opening a file

myfile.mode #checking the mode in which a file has been opened

myfile.read() #method that returns the entire content of a file in the form of a string

myfile.read(5) #returning only the first 5 characters (bytes) in the file

myfile.seek(0) #moving the cursor at the beginning of the file

myfile.tell() #checking the current position of the cursor inside the file

myfile.readline() #returns the file content one line a ta time, each time you use the method

myfile.readlines() #returns a list where each element is a line in the file

#Files - writing and appending to a file
newfile = open("newfile.txt", "w") #opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist and overrides the file if the file already exists; remember to close the file after writing to it to save the changes!

newfile.writelines(["Cisco", "Juniper", "HP", "\n"]) #this method takes a sequence of strings as an argument and writes those strings to the file

newfile = open("newfile.txt", "a") #opening a file for appending

newfile = open("newfile.txt", "w+") #opens a file for both writing and reading at the same time

newfile = open("newfile.txt", "x") #opens for exclusive creation, failing if the file already exists

#Files - closing a file
newfile.closed #checking if a file is closed

newfile.close() #closing a file

with open("python.txt", "w") as f: #using the with-as solution, the files gets closed automatically, without needing the close() method
    f.write("Hello Python!\n")
