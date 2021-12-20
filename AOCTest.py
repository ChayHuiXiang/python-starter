import requests
from bs4 import BeautifulSoup

for i in range(100):
    if i%2 == 1:
        url = 'http://10.10.123.71/api/'+str(i)
        page = requests.get(url)
        print(page.json(),url)