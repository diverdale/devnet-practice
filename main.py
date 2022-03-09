import requests
import json
import urllib3
from config import *

urllib3.disable_warnings()

url = BASE_URL + '?lat=' + LATITUDE + '&lon=' + LONGITUDE + '&appid=' + API_KEY
print(url)
weather = requests.get(url, verify=False)
print(weather.json())
