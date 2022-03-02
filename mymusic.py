import os
import eyed3

dirname = 'el musica'

os.chdir('/home/mt/Music/' + dirname)
files = os.listdir()

myfile = open('/home/mt/' + dirname, 'w')
for file in files:
    try:
        
        audio = eyed3.load(file).tag
        artist = audio.artist
        title = audio.title
        album = audio.album

        if artist is not None:
            myfile.write(artist)
        if title is not None:
            myfile.write(' --- ' + title + '\n')
    
        print(artist, end ='   ' )
        print(title)
    except:
        print('Atribute error')
