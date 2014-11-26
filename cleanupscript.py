#! /usr/bin/env python3
import os
import shutil

#Define function for moving files
def move_function(args, dir):
    count = 0
    for i in args:
        shutil.move(args[count], dir)
        count = count + 1


print ("This script is designed to cleanup the Home folder")
print ("Starting with the Downloads Folder in /home/$USER")

#Creating homedir variable
homedir = os.environ['HOME']

#Creating downloaddir variable
downloaddir = homedir + "/Downloads/"

#Creating picturedir variable
picturedir = homedir + "/Pictures/"

#Creating documentdir variable
documentdir = homedir + "/Documents/"

#Creating musicdir variable
musicdir = homedir + "/Music/"

#Creating videodir variable
videodir = homedir + "/Videos/"

print ("Moving to the /home/$USER/Downloads folder")
os.chdir(downloaddir)
file_list_docs = []
for root, dirs, files in os.walk(downloaddir):
    for f_name in files:
        if f_name.endswith('.doc'):
            file_list_docs.append(f_name)
        if f_name.endswith('.docx'):
            file_list_docs.append(f_name)
        if f_name.endswith('.pdf'):
            file_list_docs.append(f_name)
move_function(file_list_docs, documentdir)

file_list_pics = []
for root, dirs, files in os.walk(downloaddir):
    for f_name in files:
        if f_name.endswith('.jpg'):
            file_list_pics.append(f_name)
        if f_name.endswith('.png'):
            file_list_pics.append(f_name)
        if f_name.endswith('.gif'):
            file_list_pics.append(f_name)
move_function(file_list_pics, picturedir)

file_list_video = []
for root, dirs, files in os.walk(downloaddir):
    for f_name in files:
        if f_name.endswith('.mp4'):o.O
            file_list_video.append(f_name)
        if f_name.endswith('.flv'):
            file_list_video.append(f_name)
        if f_name.endswith('.mkv'):
            file_list_video.append(f_name)
move_function(file_list_video, videodir)

file_list_music = []
for root, dirs, files in os.walk(downloaddir):
    for f_name in files:
        if f_name.endswith('.mp3'):
            file_list_music.append(f_name)
        if f_name.endswith('.m4a'):
            file_list_music.append(f_name)
        if f_name.endswith('.ogg'):
            file_list_music.append(f_name)
        if f_name.endswith('.flac'):
            file_list_music.append(f_name)
move_function(file_list_music, musicdir)

print("Moving to /home/$USER/ Directory")
os.chdir(homedir)

file_list_docs[]
for root, dirs, files in os.walk(homedir):
    for f_name in files:
        if f_name.endswith('.docx'):
            file_list_docs.append(f_name)
        if f_name.endswith('.doc'):
            file_list_docs.append(f_name)
        if f_name.endswith('.pdf'):
            file_list_docs.append(f_name)
move_function(file_list_docs, documentdir)

file_list_pics = []
for root, dirs, files in os.walk(homedir):
    for f_name in files:
        if f_name.endswith('.jpg'):
            file_list_pics.append(f_name)
        if f_name.endswith('.png'):
            file_list_pics.append(f_name)
        if f_name.endswith('.gif'):
            file_list_pics.append(f_name)
move_function(file_list_pics, picturedir)

file_list_video = []
for root, dirs, files in os.walk(homedir):
    for f_name in files:
        if f_name.endswith('.mp4'):
            file_list_video.append(f_name)
        if f_name.endswith('.mkv'):
            file_list_video.append(f_name)
        if f_name.endswith('.flv'):
            file_list_video.append(f_name)
move_function(file_list_video, videodir)

file_list_music = []
for root, dirs, files in os.walk(homedir):
    for f_name in files:
        if f_name.endswith('.mp3'):
            file_list_music.append(f_name)
        if f_name.endswith('.flac'):
            file_list_music.append(f_name)
        if f_name.endswith('.m4a'):
            file_list_music.append(f_name)
        if f_name.endswith('.ogg'):
            file_list_music.append(f_name)
move_function(file_list_music, musicdir)
