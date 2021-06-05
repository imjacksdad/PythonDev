from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib.request import urlopen

url = urlopen("https://www.census.gov/programs-surveys/popest.html")
soup = BeautifulSoup(url)

with open("CensusTask_wfunction.csv","w+",newline="") as f:
        
    cwf=csv.writer(f)
    for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
        def filterunique(link):
            linklist = []
            for x in link:
                if x not in linklist:
                    linklist.append(x)

    for x in linklist:
        cw.writerow([link.get('href')])                  

        
f.close()