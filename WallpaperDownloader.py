
import WeatherGetter, os, requests, random
from bs4 import BeautifulSoup
from PIL import Image
from io import open


def getExtention(string):
    lastDot = string.rfind(".")
    size = len(string)
    if lastDot > 0:
        return string[lastDot:size].lower()
    else:
        return None

def downloadWallpapersFromURL(url,path):
    print("DOWNLOADING FROM",url,"To folder: ",path)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')

    #find how many wallpapers are available
    header = soup.find("header", class_="listing-header")
    amountOfWalls = []
    for char in header.h1.text:
        numbers = "0123456789"
        if char in numbers:
            amountOfWalls+=[char]
    amountOfWalls = "".join(amountOfWalls)
    print(int(amountOfWalls))


    #generate random numbers to decide what wallpapers to download; max 24 per page
    wallsToDownload = []

    n = random.randint(10,23)
    if int(amountOfWalls) < 24:
        n = random.randint(n/2,n)

    for x in range(n): #could be higher range if i implement the post to load more pictures. TODO
        randomWall = random.randint(0,n)
        while randomWall in wallsToDownload:
            randomWall = random.randint(0, n)
        wallsToDownload += [randomWall]
    print(wallsToDownload)

    previews = soup.find_all("a",class_="preview")

    WALLPAPERSITEURL = "https://alpha.wallhaven.cc/wallpaper/"
    WALLPAPERFULLPATH = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-"

    for num in wallsToDownload:
        print("Downloading num" + str(num))
        wallsite = requests.get(previews[num].get('href'))
        wallsoup = BeautifulSoup(wallsite.text,'html.parser')
        wallpapersrc = "https:"+wallsoup.find("img",id="wallpaper").get('src')

        import shutil

        wallpaperfile = requests.get(wallpapersrc, stream=True)
        if wallpaperfile.status_code == 200:
            with open(path+str(num)+getExtention(wallpapersrc), 'wb') as f:
                wallpaperfile.raw.decode_content = True
                shutil.copyfileobj(wallpaperfile.raw, f)


                #wallpaperfile = requests.get(wallpapersrc)
        #i =  Image.open(wallpaperfile.raw)
        print(wallpapersrc)


def downloadWallpapers(cwd,wpfoldername):
    wtdict = WeatherGetter.WEATHERTYPES
    WORKINGDIR = cwd
    WALLPAPERFOLDERNAME = wpfoldername
    os.chdir(WORKINGDIR)
    dlstrings = {}
    for key in wtdict:
        val = wtdict[key]
        dlstrings[val] = "https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&atleast=1920x1080&sorting=relevance&order=desc&page=2".format(val)
        print(dlstrings[val])

    # Make a folder for each categor


    if not(os.path.exists(WALLPAPERFOLDERNAME)):
        os.makedirs(WALLPAPERFOLDERNAME)
    os.chdir(os.path.join(os.getcwd(), WALLPAPERFOLDERNAME))
    wallpaperfolderpath = os.getcwd()+"\\"

    for key in dlstrings:
        os.chdir(wallpaperfolderpath)
        if not os.path.exists(key):
                    os.makedirs(key)
                    print('made ', os.path.join(os.getcwd(), key))
        os.chdir(os.path.join(WORKINGDIR, WALLPAPERFOLDERNAME, key) + "\\")
        cursubfolderpath = os.getcwd()+"\\"
        downloadWallpapersFromURL(dlstrings[key],cursubfolderpath)


if __name__ == "__main__":
    downloadWallpapers(os.getcwd(),"Wallpaper")


#https://alpha.wallhaven.cc/search?q=thunderstorm&categories=111&purity=100&atleast=1920x1080&sorting=relevance&order=desc&page=2
