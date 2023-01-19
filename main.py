import requests
import pickle
import http.client
import email
import os
import shutil


def auth():
    print("Hi "+str(os.environ.get("USERNAME"))+" to our application")
    conn = http.client.HTTPSConnection("api.mojoauth.com")
    uemail = input("Please enter your email:")
    payload = "{\n    \"email\": \"%s\"\n}" % (uemail)
    headers = {
        'X-API-Key': '66e863d0-698d-4743-98c2-0999d2db9a82',
        'X-API-Secret': 'c986q3qmfl6iegdvqvog.eCcPsrrEktM9oHduvAzfPL',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/users/magiclink", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    print()
    print("Please check your email for verification ..")
    print("We will wait :)")
    ids = data.decode('utf-8')[13:-2]
    conn.request("GET", "/users/status?state_id=%s" % (ids), payload, headers)
    res = conn.getresponse()
    data = res.read()
    while data.decode('utf-8') == '{"authenticated":false}':
        conn.request("GET", "/users/status?state_id=%s" %(ids), payload, headers)
        res = conn.getresponse()
        data = res.read()
    else:
        print('Verified Sucessfully')
        email = uemail
auth()

class Check:
    def __init__(self, file_format, destination):
        self.ff = file_format
        self.d = destination

    def checker(self):
        lst=os.listdir(self.d)
        #print(lst) DEBUG
        #lst.remove("dest_f")
        if (str(self.ff)+"_Files") not in lst:
            return False
        else:
            return True

    def directoryMaker(self):
        if self.checker() == False:
            os.mkdir(str(self.d)+"/"+str(self.ff)+"_Files")


class Mover:
    def __init__(self, path, source_path, destination_path, file_format):
        self.path = path
        self.source = source_path
        self.destination = destination_path
        self.ff = file_format

    def before_implementation(self):
        print("Before implenmentation, available files are: ")
        k = os.listdir(self.path)
        for i in k:
            print(i, end="\n")

    def final_move(self):
        #print(self.destination,":DEBUG")
        shutil.move(self.source, self.destination)
        print("File: "+self.source+" moved.")
        #print("FILE moved: DEBUG")


class Files:
    def __init__(self, path, dest):
        self.path = path
        self.destination = dest
        self.fff = []
        self.filenames=[]

    def File_find(self):
        for i in os.listdir(self.path):
            self.filenames.append(i)
            if '.' in i:
                file_format = i[i.index('.')+1:]
                self.fff.append(file_format)
        self.filenames.remove("dest_f")
        return self.fff

    def direcory_implement(self):
        u = self.File_find()
        for i in u:
            x = Check(i, self.destination)
            #print(self.destination,"DEBUG")
            x.directoryMaker()

    def moving(self):
        for i in self.filenames:
            source_path = self.path+'/'+str(i)
            destination_path = self.destination+"/"+(i.split(".")[-1]+"_Files")
            x = Mover(self.path, source_path, destination_path, i)
            x.final_move()


# def main():
# 	# path
# 	path = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder'

# 	# List files and directories
# 	# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
# 	print("Before moving file: ")
# 	print(os.listdir(path))


# 	for filename in os.listdir(path):
# 	    # Source path
# 	    source = 'D:/Arnav/EDU/IIITD_Material//ini_folder/' + str(filename)

# 	    # Destination path
# 	    destination = 'D:/Arnav/EDU/IIITD_Material//dest_folder'

# 	    # Move the content of
# 	    # source to destination
# 	    dest = shutil.move(source, destination)
# 	    print("File:"+filename+"moved")
# 	    file_format = 'null'
# 	    if '.' in filename:
# 	        file_format = filename[filename.index('.')+1:]
# 	    x = Check(file_format, destination)
# 	    x.directoryMaker()


def control():
    print("-------------------------------------------------------------")
    print("            Welcome to File Functionality Platform")
    print("-------------------------------------------------------------")
    print("")
    print("")
    print("-------------------------------------------------------------")
    print("Your available options are:")
    print("--------------------------------------------------------------")
    print("")
    print("1. Reorganise a cluttered folder on the basis of file format")
    print("2. Move all files of a directory to a specific folder(Gen BKP)")
    print("")
    print("-------------------------------------------------------------")
    print("")
    h = int(input("Your choice?(1/2)"))
    if(h == 1):
        path = "D:/Arnav/temp work/test1"
        #path = input("Please enter the target path:")
        destination = "D:/Arnav/temp work/test1/dest_f"
        #destination = input("Please enter the target destination:")
        k = Files(path, destination)
        k.direcory_implement()
        k.moving()
    elif(h==2):#Ext transfer
        path = "D:/Arnav/temp work/test1"
        #path = input("Please enter the target path:")
        destination = "D:/Arnav/BKP/test1"
        #destination = input("Please enter the target destination:")
        for i in os.listdir(path):
            file=path+"/"+str(i)
            send=destination+"/"+str(i)
            try:
                shutil.copy(file,send)
            except PermissionError:
                #print(i,":DEBUG")
                print("Permission Denied, Skipping folders")	
        k = Files(destination, destination+"/"+"dest_f")
        k.direcory_implement()
        k.moving()		
control()        
