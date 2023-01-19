import os
import shutil

# path
path = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder'

# List files and directories
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
print("Before moving file: ")
print(os.listdir(path))


class Check:
    def __init__(self, file_format, destination):
        self.ff = file_format
        self.d = destination

    def checker(self):
        if self.ff not in os.listdir(self.d):
            return False
        else:
            return True

    def directoryMaker(self):
        if self.checker == False:
            os.mkdir(self.ff)


for filename in os.listdir(path):
    # Source path
    source = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder/' + \
        str(filename)

    # Destination path
    destination = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/dest_folder'

    # Move the content of
    # source to destination
    dest = shutil.move(source, destination)
    print("File:"+filename+" moved")
    file_format = 'null'
    if '.' in filename:
        file_format = filename[filename.index('.')+1:]
    x = Check(file_format, destination)
    x.directoryMaker()
