import requests
import pprint
import json
import urllib3
from config import *

pp = pprint.PrettyPrinter(indent=4)

urllib3.disable_warnings()

url = BASE_URL + '?lat=' + LATITUDE + '&lon=' + LONGITUDE + '&exclude=minutely,hourly&units=imperial&appid=' + API_KEY
weather_dale = requests.get(url, verify=False)
print(weather_dale.json()['current'])
#pp.pprint(weather.json())
