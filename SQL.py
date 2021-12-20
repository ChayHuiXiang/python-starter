import sqlite3
conn=sqlite3.connect("emaildb.sqlite")
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname=input("Enter File Name:")
if len(fname)<1: fname="mbox.txt"
fhand=open(fname)

for line in fhand:
    if not line.startswith("From "): continue
    words=line.split()
    fullemail=words[1]
    splitemail=fullemail.split("@")
    email=splitemail[1]
    cur.execute("SELECT count FROM Counts WHERE org=?",(email,))
    row=cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts(org,count)VALUES(?,1)",(email,))
    else:
        cur.execute("UPDATE Counts SET count=count+1 WHERE org=?",(email,))
conn.commit()

cur.execute("SELECT * FROM Counts ORDER BY count DESC LIMIT 10")
for row in cur:
    print(row[0],row[1])

conn.close()