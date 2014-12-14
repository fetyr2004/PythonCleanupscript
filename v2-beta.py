#! /usr/bin/env python3
import os
import shutil
def move_function(args, directory):
	shutil.move(args, directory)
# Creatinge Home Directory for reference
homedir = os.environ['HOME']
homedir = homedir + "/"
downloaddir = homedir + "Downloads"

# reading file
with open('config', encoding='utf-8') as a_file:
		for a_line in a_file:
			line = a_line[:1]
			if (line == "*"):
				extractdir = a_line[1::]
				workingdir = homedir + extractdir
				print(workingdir)
			if (line == "#"):
				os.chdir(downloaddir)
				file_extension = a_line[1::]
				file_extension = file_extension.rstrip('\n')
				for root, dirs, files in os.walk(downloaddir):
					for f_name in files:
						if f_name.endswith(file_extension):
							print(f_name)
							print(workingdir)
							shutil.move(f_name, workingdir)



