
from bs4 import BeautifulSoup
import requests
import re

from urllib.request import urlopen
url=urlopen('https://www.census.gov/programs-surveys/popest.html')

soup = BeautifulSoup(url)

list(soup.children)

##for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
##    print (link.get('href'))
##
##list_of_urls = ['url_1', 'url_1', 'url_2', 'url_1', 'url_1', 'url_2', 'url_3', 'url_3'] 
##set_of_urls = set(list_of_urls) # return : {'url_1', 'url_2', 'url_3'}
##list_clean = list(set_of_urls) # return :['url_3', 'url_1', 'url_2']
##
##
##
##import csv
##for link in results:
##    S=link.get('href')
##    csvRow = [S]
##    csvfile = "urls1.csv"
##    with open(csvfile, "a") as fp:
##        wr = csv.writer(fp, dialect='excel')
##        wr.writerow(csvRow )
