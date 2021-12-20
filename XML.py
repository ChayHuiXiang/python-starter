#In this assignment you will write a Python program 
# somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL 
# using urllib and then parse and 
# extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.

import xml.etree.ElementTree as ET
import urllib.error,urllib.parse,urllib.request
count=0
sum=0
url=input("Enter url:")
fhand=urllib.request.urlopen(url).read()
data=ET.fromstring(fhand)

comments=data.findall("comments/comment") #or findall('.//count')
for comment in comments:
    count=int(comment.find("count").text)
    sum=sum+count
print(sum)