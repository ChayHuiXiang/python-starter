#In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/json2.py. The program will prompt for a URL, 
# read the JSON data from that URL using urllib and then parse and 
# extract the comment counts from the JSON data, compute the sum of the numbers in the file and 
# enter the sum below:

import json
import urllib.parse,urllib.error,urllib.request
url=input("Enter Url:")
fhand=urllib.request.urlopen(url)
data=fhand.read().decode()
js=json.loads(data)
sum=0
for name in js["comments"]:
    count=int(name["count"])
    sum=sum+count
print(sum)