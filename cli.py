import BackgroundChanger,WeatherGetter,WallpaperDownloader,WallpaperSelector

import time, os


#todo Unit tests boi



def startProgram():
    WALLPAPERFOLDERNAME = "Wallpapers"
    WORKINGDIR = os.getcwd()  # TODO: VERANDEREN KUT
    INTERVAL = 1  # TODO: veranderen in minuten, secondes en uren | in cfg of interface

    numofWalls = 0  # misschien leuk stat bestandje van maken

    print("Starting WallChanger! Press ctrl+c, or close this window to quit.")
    while True:
        os.chdir(WORKINGDIR)

        print("Wallpaper number ",numofWalls, "@ ",time.strftime("%H:%M:%S", time.localtime(time.time())),"==>",WallpaperSelector.selectWallpaper(WORKINGDIR, WALLPAPERFOLDERNAME))

        numofWalls += 1

        time.sleep(INTERVAL*60)
if __name__ == "__main__":
    while True:
        time.sleep(1)
        inp = input("S: Start Wallchanger | D: Download Wallpapers:  ")
        if inp in "sS":
            startProgram()
        elif inp in "dD":
            WallpaperDownloader.downloadWallpapers(WORKINGDIR,WALLPAPERFOLDERNAME)