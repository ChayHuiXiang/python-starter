import json
import sqlite3

conn=sqlite3.connect("coursedb.sqlite")
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE "Course" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "User" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "Member" (
	"course_id"	INTEGER,
	"user_id"	INTEGER,
	"role"	INTEGER
);

''')

fname=input("ENTER FILE NAME:")
if len(fname)<1: fname="roster_data.json"
fhand=open("roster_data.json").read()
js=json.loads(fhand)
print(js)

for data in js:
    user=data[0]
    course=data[1]
    role=data[2]

    cur.execute("INSERT OR IGNORE INTO Course(title) VALUES (?)",(course,))
    cur.execute("SELECT id FROM Course WHERE title=?",(course,))
    course_id=cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO User(name) VALUES (?)",(user,))
    cur.execute("SELECT id FROM User WHERE name=?",(user,))
    user_id=cur.fetchone()[0]

    print(user,course,role,user_id,course_id)

    cur.execute("INSERT OR REPLACE INTO Member(course_id,user_id,role) VALUES (?,?,?)",(course_id,user_id,role))

conn.commit()
conn.close()