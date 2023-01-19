import requests
import pickle
import http.client
import email
import os
import shutil


def auth(self):
    conn = http.client.HTTPSConnection("api.mojoauth.com")
    uemail = input("Please enter your email:")
    payload = "{\n    \"email\": \"%s\"\n}" % (uemail)
    headers = {
        'X-API-Key': '',
        'X-API-Secret': '',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/users/magiclink", payload, headers)
    res = conn.getresponse()
    data = res.read()
    #print(data.decode("utf-8"))
    print()
    print("Please check your email for verification ....")
    print("We will wait for  you :)")
    ids = data.decode('utf-8')[13:-2]
    conn.request("GET", "/users/status?state_id=%s" % (ids), payload, headers)
    res = conn.getresponse()
    data = res.read()
    while data.decode('utf-8') == '{"authenticated":false}':
        conn.request("GET", "/users/status?state_id=%s" %
                    (ids), payload, headers)
        res = conn.getresponse()
        data = res.read()
    else:
        print('verified Sucessfully')
        email = uemail



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
        if self.checker() == False:
            os.mkdir(self.ff)


'''
# path
path = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder'

# List files and directories
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
print("Before moving file: ")
print(os.listdir(path))


for filename in os.listdir(path):
    # Source path
    source = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder/' + \
        str(filename)

    # Destination path
    destination = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/dest_folder'

    # Move the content of
    # source to destination
    dest = shutil.move(source, destination)
    print("File:"+filename+"moved")
    file_format = 'null'
    if '.' in filename:
        file_format = filename[filename.index('.')+1:]
    x = Check(file_format, destination)
    x.directoryMaker()'''


class Mover:
    def __init__(self, path, source_path, destination_path, file_format):
        self.path = path
        self.source = source_path
        self.destination = destination_path
        self.ff = file_format

    

    def before_implementation(self):
        print("Before implenmentation: ")
        k = os.listdir(self.path)
        print(k)

    def fileTreverse(self):
        for i in os.listdir(self.path):
            source_main = self.source + "/" + str(i)
            destination_main = shutil.move(self.source, self.destination)
            if '.' in i:
                self.ff = i[i.index('.')+1:]
            x = Check(self.ff, self.destination)
            x.directoryMaker()
