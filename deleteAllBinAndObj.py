# 1/8/19
# Written by Guy Kaplan
# This Python script deletes all bin and obj folders from a given folder.
# Namely user gives the folder path during the script.
# If no path is given, it deletes from the current folder (by default).

import os
import shutil
import sys

numOfRemovedFolders = 0
print("This script deletes all bin and obj folders from a single folder.")
rootFolder = input("Enter a valid folder path (press Enter for the current cmd path): ")
if rootFolder == "":
	# set rootFolder to current cmd path folder
	rootFolder = os.getcwd()
if not os.path.isdir(rootFolder):
	print("Error: given folder does NOT exist")
	sys.exit()
print("--Deleting all bin and obj folders from root folder: {}--".format(rootFolder))
for root, dirs, files in os.walk(rootFolder):
	for name in dirs:
		if name == "bin" or name == "obj":
			shutil.rmtree(os.path.join(root, name), ignore_errors=True)
			numOfRemovedFolders += 1
print("Removed {} folders".format(numOfRemovedFolders))






