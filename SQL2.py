import sqlite3
import xml.etree.ElementTree as ET

conn=sqlite3.connect("itunesdb.sqlite")
cur=conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

fname=input("Enter File Name:")
if len(fname)<1: fname="Library.xml"
fhand=open(fname)
data=fhand.read()
xml=ET.fromstring(data)

def lookup(d,key):
    found=False
    for child in d:
        if found: return child.text
        if child.tag=="key" and child.text==key:
            found=True
    return None

tracks=(xml.findall("dict/dict/dict"))
for track in tracks:
    ID=lookup(track,"Track ID")
    if ID is None: continue
    name=lookup(track,"Name")
    length=lookup(track,"Total Time")
    Album=lookup(track,"Album")
    Genre=lookup(track,"Genre")
    Rating=lookup(track,"Rating")
    Count=lookup(track,"Play Count")
    Artist=lookup(track,"Artist")

    print(ID,name,length,Album,Genre,Rating,Count,Artist)

    if Artist is None or Genre is None or Album is None: continue
    cur.execute("INSERT OR IGNORE INTO Artist(name) VALUES (?)",(Artist,))
    cur.execute("SELECT id from Artist WHERE name=?",(Artist,))
    artist_id=cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Genre(name) VALUES (?)",(Genre,))
    cur.execute("SELECT id from Genre WHERE name=?",(Genre,))
    genre_id=cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album(title,artist_id) VALUES (?,?)",(Album,artist_id))
    cur.execute("SELECT id from Album WHERE title=?",(Album,))
    album_id=cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track(title,album_id,genre_id,len,
    rating,count) VALUES (?,?,?,?,?,?)''',(name,album_id,genre_id,length,Rating,Count))

conn.commit()