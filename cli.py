import BackgroundChanger,WeatherGetter,WallpaperDownloader,WallpaperSelector,Settings

import time, os


#todo Unit tests boi



def startProgram():
    currentSettings = Settings.getSettings()
    WALLPAPERFOLDERNAME = "Wallpapers"
    WORKINGDIR = currentSettings["wpLocation"]  # TODO: Checken of de waardes kloppen
    INTERVAL = currentSettings["delay"]  # TODO: veranderen in minuten, secondes en uren en checken
    CITY = currentSettings["city"]

    numofWalls = 0  # misschien leuk stat bestandje van maken

    print("Starting WallChanger! Press ctrl+c, or close this window to quit.")
    while True:
        os.chdir(WORKINGDIR)

        print("Wallpaper number ",numofWalls, "@ ",time.strftime("%H:%M:%S", time.localtime(time.time())),"==>",
              WallpaperSelector.selectWallpaper(WORKINGDIR, WALLPAPERFOLDERNAME),"in",CITY) #TODO Format?

        numofWalls += 1

        time.sleep(INTERVAL*60)
if __name__ == "__main__":
    while True:
        time.sleep(1)
        inp = input("S: Start Wallchanger | D: Download Wallpapers | C: Change Settings:  ")
        if inp in "sS":
            startProgram()
        elif inp in "dD":
            WallpaperDownloader.downloadWallpapers(WORKINGDIR,WALLPAPERFOLDERNAME)
        elif inp in "cC":
            print("Current Settings:")
            settings = Settings.getSettings()
            settingnum = {}
            for idx,key in enumerate(settings):
                print(" {} | {:<13}:  {}".format(idx,key,settings[key]))
                settingnum[idx] = key
            print(settingnum)
            print("\n\n")
            print("What setting do you want to change? Press enter to cancel.")
            settingtochange = input("Please enter one of the numbers shown above: ")
            if settingtochange == "":
                break
            while not(settingtochange.isnumeric()) or not(int(settingtochange) <=idx):
                print(settingtochange, enumerate(settings))
                print("No valid number was entered. Please try again. Insert enter to cancel...")
                settingtochange = input("Please enter one of the numbers shown above: ")
                if settingtochange == "":
                    break

            settingname = settingnum[int(settingtochange)]
            changedval = input("Please insert the value you want to change {} into:".format(settingname))



            if  isinstance(settings[settingname], int) or str(settings[settingname]).isnumeric():
                while not( str(changedval).isnumeric() )or not( isinstance(settings[settingname], int)):
                    if changedval == "":
                        break
                    print("That is not a number! Please try again or press Enter to exit:")
                    changedval = input("Please insert the value you want to change {} into:".format(settingname))


                if not (changedval == ""):
                    Settings.changeSettings(settingname, int(changedval))
                    print("{} changed to: {}".format(settingname, changedval))

            elif os.path.exists(os.path.dirname(settings[settingname])):
                while not os.path.exists(os.path.dirname(changedval)):
                    if changedval == "":
                        break
                    print("That folder does not exist! Please try again or press Enter to exit:")
                    changedval = input("Please insert the value you want to change {} into:".format(settingname))


                if not (changedval == ""):
                    Settings.changeSettings(settingname,changedval)
                    print("{} changed to: {}".format(settingname, changedval))

            else:
                if not (changedval == ""):
                    Settings.changeSettings(settingname,changedval)
                    print("{} changed to: {}".format(settingname, changedval))
                else:
                    continue

