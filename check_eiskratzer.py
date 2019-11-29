#!/usr/bin/env python3

import argparse
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--apikey', required=True, type=str, help='API Key - https://www.eiswarnung.de/rest-api/')
parser.add_argument('-a', '--latitude', required=True, type=float, help='latitude eg. 51.397933')
parser.add_argument('-o', '--longitude', required=True, type=float, help='longitude eg. 12.399797')
args = parser.parse_args()

payload = {'key': args.apikey,
           'lat': args.latitude,
           'lng': args.longitude}

try: 
    r = requests.post('https://api.eiswarnung.de', params=payload)
    r.raise_for_status()
    j = r.json()
except Exception as e: 
    print(e)
    sys.exit(3)
    
api_status = {
    200: 'Aufruf erfolgreich',
    300: 'Geokoordinaten fehlen',
    400: 'API Key fehlt',
    401: 'API Key ungültig',
    402: 'Tägliches Call-Limit erreicht'
}

if j["success"] != True or j["code"] != 200:
    print("UNKNOWN: " + api_status.get(j["code"],"UNKNOWN STATUS"))
    sys.exit(3)

print("%s in %s am %s" % 
      (j["result"]["forecastText"][:-1], 
       j["result"]["forecastCity"],
       j["result"]["forecastDate"])
     )

if j["result"]["forecastId"] == 0:
    # KEIN EIS
    sys.exit(0)
elif j["result"]["forecastId"] == 1:
    # EIS
    sys.exit(2)
elif j["result"]["forecastId"] == 2:
    # EVTL EIS
    sys.exit(1)
else:
    # UNKNOWN
    sys.exit(3)
