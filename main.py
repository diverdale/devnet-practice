import requests
import pprint
import json
import urllib3
from config import *

pp = pprint.PrettyPrinter(indent=4)

urllib3.disable_warnings()

url = BASE_URL + '?lat=' + LATITUDE + '&lon=' + LONGITUDE + '&appid=' + API_KEY
weather = requests.get(url, verify=False)
pp.pprint(weather.json())
