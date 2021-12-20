#In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/geojson.py. The program will prompt for a location, 
# contact a web service and retrieve JSON for the web service and parse that data, 
# and retrieve the first place_id from the JSON. A place ID is a textual identifier that 
# uniquely identifies a place as within Google Maps.

import json
import urllib.error,urllib.parse,urllib.request

location=input("Enter a Location:")
API="http://py4e-data.dr-chuck.net/json?"
url=API+urllib.parse.urlencode({"address":location,"key":42})
fhand=urllib.request.urlopen(url)
data=fhand.read().decode()
js=json.loads(data)
place=js["results"][0]["place_id"]
print(place)