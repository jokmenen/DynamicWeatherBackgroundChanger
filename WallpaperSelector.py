import os
import random

import BackgroundChanger
import WallpaperDownloader
import WeatherGetter


# Set a wallpaper based on the current weather
def selectWallpaper(cwd,wpfoldername):
    WALLPAPERFOLDERNAME = wpfoldername
    if os.path.exists(WALLPAPERFOLDERNAME):
        currentWeather = WeatherGetter.getWeather()
        os.chdir(os.path.join(os.getcwd(),WALLPAPERFOLDERNAME,currentWeather))
        randwall = os.listdir()[random.randint(0,len(os.listdir())-1)]
        randwallfullpath = os.path.join(os.getcwd(),randwall)
        BackgroundChanger.setWallpaper(randwallfullpath)
        return currentWeather
    else:
        print("Wallpapers File Does Not Yet Exist! Want to download some wallpapers?")
        input = ""
        while not( input == "n" or input == "y"):
            input = input("Download wallpapers? (y/n):    ")
            if input == "y":
                WallpaperDownloader.downloadWallpapers(cwd,wpfoldername)
                print("Restart the program to continue")
                quit()
            elif input == "n":
                quit()

if __name__ == "__main__":
    selectWallpaper(os.getcwd(),"Wallpaper")