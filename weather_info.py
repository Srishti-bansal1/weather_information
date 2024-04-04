import requests
from geopy.geocoders import Nominatim

class DynamicData:
    def __init__(self):
        pass

    def weather_lang_long(self,location):
        loc = Nominatim(user_agent="Geopy Library")
        getLoc = loc.geocode(location)
        print(location)
        print(getLoc.latitude, getLoc.longitude)
        return getLoc.latitude, getLoc.longitude

    def get_weather(self,_location):
        x,y = self.weather_lang_long(_location)
        weather_api_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=ff9e335caf44a838adff7eb19b448759".format(x,y)
        weather = requests.get(weather_api_url)
        data = weather.json()
        return data

weather_info = DynamicData()
_location = input("enter the location:")
print(weather_info.get_weather(_location))