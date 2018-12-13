import os
import random
import requests
from PIL import Image
from bs4 import BeautifulSoup
from io import open

import WeatherGetter


# There was a better way for this function but I can't remember it now.
def getExtention(string):
    lastDot = string.rfind(".")
    size = len(string)
    if lastDot > 0:
        return string[lastDot:size].lower()
    else:
        return None


# Go to the passed url to download some nice Weather related wallpapers for use in the program.
# Currently only works for Wallhaven urls,
def downloadWallpapersFromURL(url,path):
    print("DOWNLOADING FROM",url,"To folder: ",path)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')

    # Find how many wallpapers are available
    header = soup.find("header", class_="listing-header")
    amountOfWalls = []
    for char in header.h1.text:
        numbers = "0123456789"
        if char in numbers:
            amountOfWalls += [char]
    amountOfWalls = "".join(amountOfWalls)
    print(int(amountOfWalls))

    # Generate random numbers to decide what wallpapers to download; max 24 per page
    wallsToDownload = []

    n = random.randint(10, 23)
    if int(amountOfWalls) < 24:
        n = random.randint(n / 2, n)

    for x in range(n): #could be higher range if i implement the post to load more pictures. TODO
        randomWall = random.randint(0,n)
        while randomWall in wallsToDownload:
            randomWall = random.randint(0, n)
        wallsToDownload += [randomWall]
    print(wallsToDownload)

    previews = soup.find_all("a", class_="preview")

    for num in wallsToDownload:  # Download the wallpapers...
        print("Downloading num" + str(num))
        wallsite = requests.get(previews[num].get('href'))
        wallsoup = BeautifulSoup(wallsite.text, 'html.parser')
        wallpapersrc = "https:"+wallsoup.find("img",id="wallpaper").get('src')

        import shutil

        # ... And copy them to the passed location
        wallpaperfile = requests.get(wallpapersrc, stream=True)
        if wallpaperfile.status_code == 200:
            with open(path+str(num)+getExtention(wallpapersrc), 'wb') as f:
                wallpaperfile.raw.decode_content = True
                shutil.copyfileobj(wallpaperfile.raw, f)


                #wallpaperfile = requests.get(wallpapersrc)
        #i =  Image.open(wallpaperfile.raw)
        print(wallpapersrc)


def downloadWallpapers(cwd, wpfoldername):
    wtdict = WeatherGetter.WEATHERTYPES  # Get the types of weather supported by this program
    WORKINGDIR = cwd
    WALLPAPERFOLDERNAME = wpfoldername
    os.chdir(WORKINGDIR)
    dlstrings = {}
    for key in wtdict:
        val = wtdict[key]
        # Fill dlstrings with urls of search results on wallhaven with all the weathertypes in wtdict
        dlstrings[val] = "https://alpha.wallhaven.cc/search?q={}&categories=111&purity=100&atleast=1920x1080&sorting=relevance&order=desc&page=2".format(val)
        print(dlstrings[val])

    # Make a folder for each category if they don't exist yet.
    if not(os.path.exists(WALLPAPERFOLDERNAME)):
        os.makedirs(WALLPAPERFOLDERNAME)
    os.chdir(os.path.join(os.getcwd(), WALLPAPERFOLDERNAME))
    wallpaperfolderpath = os.getcwd() + "\\"  # TODO make tidy

    for key in dlstrings:  # Create a folder for each weather type and download the wallpapers to the folder
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
