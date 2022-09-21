
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
    
    txt = 'gulzat'
    if not f_name.startswith('gulzat'):
        new_name = txt + '_' + f_name
    else:
        new_name = '' + f_name
    #new_name = f_name.replace('_', ''
    #print(f_name)    
    #print(new_name)
  
    os.rename(f, new_name) 
    
