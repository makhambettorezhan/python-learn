# this program takes path as string and recursively will rename
# files according to some criteria and sorted by last modification date


import os
import glob


COUNT = 1

def increment(): 
    global COUNT 
    COUNT = COUNT + 1


# Recursively print png images in folder C:\Users\admin\
path = '/home/mt/'
files = glob.iglob(path, recursive=True)
sorted_by_mtime_descending = sorted(files, key=lambda t: os.stat(t).st_mtime)

for f in sorted_by_mtime_descending:
    f_name, f_ext = os.path.splitext(f) 
    f_name = str(COUNT)
    
    if COUNT < 10:
        f_name = '00' + f_name
    elif COUNT < 100:
        f_name = '0' + f_name
    f_name = f_name + 'comics'

    increment() 

    new_name = '{} {}'.format(f_name, f_ext) 
    os.rename(f, new_name) 
    #print(filepath)
