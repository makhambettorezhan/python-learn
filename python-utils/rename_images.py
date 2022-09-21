
# Python program to rename all file 
# names in your directory  
import os 
import glob

path = '/home/mt/'
os.chdir(path) 
COUNT = 1
files = os.listdir()
# Function to increment count  
# to make the files sorted. 
def increment(): 
    global COUNT 
    COUNT = COUNT + 1
  
for f in files: 
    f_name = os.path.basename(f) 
    
    if COUNT < 10:
        f_name = '00' + f_name
    elif COUNT < 100:
        f_name = '0' + f_name
  
    os.rename(f, f_name) 
    
