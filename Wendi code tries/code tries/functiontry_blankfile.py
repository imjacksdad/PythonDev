from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib.request import urlopen

url = urlopen("https://www.census.gov/programs-surveys/popest.html")
soup = BeautifulSoup(url,features="lxml")
   
linklist = []

for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
    if link not in linklist:
        linklist.append(link.get('href'))

    setoflinks = set(linklist)
    #sorted(setoflinks)

f = open("demofile3.txt", "a")

for link in setoflinks:
    print(link)
    f.write(link)
    f.write('\n')

f.close()
   

