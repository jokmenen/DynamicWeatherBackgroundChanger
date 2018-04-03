
# sets the background to desired image
# for reference, see:
# - https://code.activestate.com/recipes/435877-change-the-wallpaper-under-windows/
# - http://www.blackwasp.co.uk/wallpaper.aspx

from ctypes import *

def setWallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
    return


if __name__ == "__main__":
    import os

    TESTFILE = "test.png"
    testpath = os.getcwd()+"\\"+TESTFILE
    setWallpaper(testpath)