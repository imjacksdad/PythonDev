
from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib.request import urlopen
url = urlopen("https://www.census.gov/programs-surveys/popest.html")

soup = BeautifulSoup(url, 'lxml')
linklist = soup.findAll('a', attrs={'href': re.compile("^http")})
linkset = []


    
##with open("CensusTask_whoopdi2.csv","w+",newline="") as f:
##        
##    cwf=csv.writer(f)
##   
for link in linklist:
    if link not in linklist:
        linkset.append(link)
    else:
        #cwf.writerow([link.get('href')])
        print([link.get('href')])
##
##        
##f.close()
