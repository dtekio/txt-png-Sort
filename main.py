import os
import shutil

path = input('Enter the path: ')
names = os.listdir(path)
folder_names = ['image', 'text']
for folder in folder_names:
    if not os.path.exists(path+folder):
        os.makedirs(path+folder)
for files in names:
    if ".png" in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files, path+"image/"+files)
    if ".txt" in files and not os.path.exists(path+'text/'+files):
        shutil.move(path+files, path+"text/"+files)