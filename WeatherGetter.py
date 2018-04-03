# Dict of weather condition codes associated with conditions
# Note: In this version I will just look at the broad weather conditions
# like clear, rain etc. and won't go into specifics.
# Therefore I will only check the first number of the code (with exception of 8 and 9)

WEATHERTYPES = {  # Could also maybe use just the weather names to search for wallpapers in advanced versions
    #Note: use + to link words (for in the url e.g. clear+skies)
    2: "Thunderstorm",
    3: "Light+Rain", #actually drizzle but it does not find anything, made it light rain so its different from 5
    5: "Rain",
    6: "Snow",
    7: "Fog",  #Was atmosphere, but that does not really get any good Backgrounds
    800: "Clear+Sky",  #used to be just clear # FFS They have to be a bitch and include clouds under this category.
    80: "Clouds",  # I will probably write an exception for this meh #edit: see comment below
    90: "Tornado",  # used to be extreme
    9: "Weather"  #used to be additional which is vague as fuck. Got no results for breeze or wind so whatever.
    # check for length of string of these numbers: because 90x is Extreme but 9XX is additional etc. Fucking OWM
}

def getWeather():
    weatherJSON = getWeatherJSON()
    currentWeatherDict = weatherJSON["weather"]
    # WTF sometimes this (v) might return more than one weather specification??? Will just use 1st.
    #if len(currentWeatherDict) > 1: nvm the ^ comment, it always does this for some reason...
    currentWeatherDict = currentWeatherDict[0]

    weatherstr = getWeatherTypeFromID(currentWeatherDict["id"])
    return weatherstr


def getWeatherJSON(): #TODO: add way to customize city
    from pprint import pprint
    import json
    import requests

    # Get the current weather from Open Weather Map API

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tilburg,nl&APPID=5bcb315696e72e6cee087d0df618811f')
    weer = r.json()
    return weer

    #Test code: used to not overload the API
    #with open("tilburgweer.json") as weerfp:
    #    weer = json.loads(weerfp.read())

    #return weer



def getWeatherTypeFromID(id):



    # Find first number in condition code,
    firstnum = int(str(id)[0]) #sorry to the reader for the shitshow of conversions



    #check if this is part of one of the codes with multiple conditions under one number

    #TODO: find a way to do this smart with regex 'n shit. Or not. Im not a police officer.
    #form: {exception number, 'Regex code to check
    #exceptions = {"8",800}
    exceptions = [8,9] #lazy solution lol

    weathercond = "404" #returns funny 404 wallpapers haha so funny good on you Jokmenen for making this.

    if firstnum in exceptions:
        if id == 800:
            weathercond = WEATHERTYPES[800]
        elif str(id)[:2] == 80:
            weathercond = WEATHERTYPES[80]
        else:
            #TODO: Add 9 and 90
            weathercond = "Tornado"

    else:
        weathercond = WEATHERTYPES[firstnum]

    return weathercond


if __name__ == "__main__":
    print(getWeather())
# IDEE TIJD:
# Maak ook een scriptje die automatisch walls download voor de weertypes voor als je daar zelf te lui voor bent
