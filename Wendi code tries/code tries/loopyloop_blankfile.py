
from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib.request import urlopen
url = urllib.request.urlopen("https://www.census.gov/programs-surveys/popest.html")
soup = BeautifulSoup(url)
censuslinks = []
censuslinks.append(f)
with open("CensusTask_whatsthis2.csv","w+",newline="") as f:
    for censuslink in censuslinks:
        for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
            if censuslink not in censuslinks:
                cwf.writerow([link.get('href')])
        

f.close()