from bs4 import BeautifulSoup
import requests
 
def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    #print(sourceCode)
    soup = BeautifulSoup(sourceCode, 'html.parser')
    #print(soup)
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
    #for link in soup:
        href = link.get('href')
        #print(href)
        if link.startswith('/watch?'):
            print(link.string.strip())
            print(domain + href + '\n')
getPlaylistLinks('https://www.youtube.com/playlist?list=PLrT4uvwaf6uw5ChxpBQnx0dA5fcmXvuB_')
