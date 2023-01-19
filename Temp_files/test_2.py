# import os
# import shutil
# #this is the folder where we have the files we want to move:
# directory = 'C:/Users/arnag/Desktop/test1_in'
# #this is the folders we are moving the files to:
# pdf_directory = ''
# img_directory = ''
# exe_directory = ''
# mp4_directory = ''
# doc_directory = 'C:/Users/arnag/Desktop/test1_in/text/'
# bok_directory = ''
# zip_directory = ''
# other_directory = ''
# juypter = ''

# #this loops over the file names in dirctory

# for filename in os.listdir (directory) :
#      if filename.endswith ('.pdf'): #to filter the files
#           os. rename (directory+'/' +filename, pdf_directory+'/'+filename)#moves the files
#      elif filename.endswith ('.jpg') or filename.endswith(".png") or filename.endswith ('jpeg') or filename.endswith ('.PNG'): # ditto
#           os. rename (directory+'/' +filename, img_directory+'/'+filename)#moves the files
#      elif filename.endswith ('.exe'): # ditto
#           os. rename (directory+'/'+filename, exe_directory+'/'+filename) # moves the files
#      elif filename.endswith ('.mp4') or filename.endswith (".mkv"): #ditto
#           os.rename (directory+'/'+filename, mp4_directory+'/'+filename) # moves the files
#      elif filename.endswith ('.doc') or filename.endswith('text'): # ditto
#           shutil.move(directory,doc_directory) #moves the files
#      elif filename.endswith ('.epub') or filename.endswith ('.mobi'): #ditto
#           os. rename (directory+'/'+filename, bok_directory+'/'+filename) #moves the files
#      elif filename.endswith ('.zip') or filename.endswith ('.rar') or filename.endswith ('.7z') or filename.endswith ('.gz'): # ditto
#           os. rename (directory+'/'+filename, zip_directory+'/'+filename) #moves the files
#      elif filename.endswith ('.ipynb'): # ditto
#           shutil.move (directory+'/'+filename, juypter+'/'+filename) #moves the files
#      else:
#           print ('other file format:' + filename)
#           shutil.move(directory+"/"+filename,doc_directory) #ditto    


# Python program to explain shutil.move() method
     
# importing os module
import os

# importing shutil module
import shutil

# path
path = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder'

# List files and directories
# in 'C:/Users/Rajnish/Desktop/GeeksforGeeks'
print("Before moving file:")
print(os.listdir(path))


# Source path
source = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/ini_folder/test1.txt'

# Destination path
destination = 'D:/Arnav/EDU/IIITD_Material/Work/Under_const/SEM1/CSE101/CSE101-OpA2-06042022/dest_folder'

# Move the content of
# source to destination
dest = shutil.move(source, destination)

# List files and directories
# in "C:/Users / Rajnish / Desktop / GeeksforGeeks"
print("After moving file:")
print(os.listdir(path))

# Print path of newly
# created file
print("Destination path:", dest)
