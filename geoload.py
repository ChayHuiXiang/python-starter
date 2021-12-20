import json
import urllib.error,urllib.parse,urllib.request
import sqlite3

conn=sqlite3.connect("geodata.sqlite")
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Locations")
cur.execute("CREATE TABLE Locations(address TEXT,geodata TEXT)")

fhand=open("where.data").read()
API="http://py4e-data.dr-chuck.net/json?"

places=fhand.split("\n")
for place in places:
    if len(place)<1: continue
    url=API+urllib.parse.urlencode({"address":place,"key":42})
    print("Retrieving",url)
    data=urllib.request.urlopen(url)
    fhand=data.read().decode()
    js=json.loads(fhand)
    cur.execute("SELECT address FROM Locations WHERE address=?",(place,))
    if cur is None:
        cur.execute("INSERT INTO Locations(address,geodata) VALUES (?,?)",(place,fhand))
    else:
        print("data found for",place)
conn.commit()