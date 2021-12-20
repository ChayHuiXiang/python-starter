import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

Count=0
Pos=0
url=input("Enter URL:")
Countinput=input("Enter Count:")
Count=int(Countinput)
Posinput=input("Enter Position:")
Pos=int(Posinput)-1
while Count!=0:
    fhand=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(fhand,"html.parser")
    anchor=soup("a")
    tag=anchor[Pos]
    url=tag.get("href",None)
    print("Retrieving:",url)
    Count=Count-1