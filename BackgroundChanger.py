
# sets the background to desired image
# for reference, see:
# - https://code.activestate.com/recipes/435877-change-the-wallpaper-under-windows/
# - http://www.blackwasp.co.uk/wallpaper.aspx

import os
import sys
from ctypes import *


def setWallpaper(path):
    if os.name != "nt":
        sys.exit("Non-Windows OS detected!. This program was made to run on Windows!")
    SPI_SETDESKWALLPAPER = 20
    windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
    return


if __name__ == "__main__":

    TESTFILE = "test.png"
    testpath = os.path.join(os.getcwd(), TESTFILE)
    setWallpaper(testpath)
