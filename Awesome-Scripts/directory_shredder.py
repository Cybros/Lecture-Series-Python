import os
import shutil
pwd = os.getcwd()
files_list = os.listdir(pwd)
for file in files_list:
	if os.path.isdir(file) == True:
		shutil.rmtree(file)
	else:
		os.remove(file)
