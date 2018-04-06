import os, json

def getSettings():

    settingsDict = {

        "wpLocation" : os.getcwd(),
        "delay" : 5,
        "city" : "Tilburg"

    }

    with open("settings.json","r") as fp:
        raw = fp.read()
        if raw:

            fpjson = json.loads(raw)
            for setting in settingsDict:
                if setting in fpjson.keys():
                    settingsDict[setting] = fpjson[setting]

    return settingsDict

def changeSettings(key,val):
    cursettings = getSettings()
    cursettings[key] = val
    with open("settings.json","w+") as fp:
        fp.write(json.dumps(cursettings))



if __name__ == "__main__":
    print(getSettings())
    changeSettings("delay",222)
    print(getSettings())