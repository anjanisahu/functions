import os
import shutil
## source path
path='C:\Users\hp\Downloads\Python\ProFunctions'
path2='C:\Users\hp\Downloads\Python\ProFunctions'
finalPath = shutil.copy(path,path2)

# Read in the file
with open('file.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('ram', 'abcd')

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)
