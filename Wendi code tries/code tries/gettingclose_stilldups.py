
from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib.request import urlopen
url = urlopen("https://www.census.gov/programs-surveys/popest.html")

soup = BeautifulSoup(url, "lxml")
list_of_urls = soup.findAll('a', attrs={'href': re.compile("^http")})

#list_of_urls = ['url_1', 'url_1', 'url_2', 'url_1', 'url_1', 'url_2', 'url_3', 'url_3'] 
##set_of_urls = set(list_of_urls) # return : {'url_1', 'url_2', 'url_3'}
##list_clean = list(set_of_urls) # return :['url_3', 'url_1', 'url_2']
print(list_of_urls)    
##with open("CensusTask_whoopdi2.csv","w+",newline="") as f:
##        
##    cwf=csv.writer(f)
##   
##    for link in linklist:
##        if link not in linklist:
##            linkset.append(link)
##        else:
##            cwf.writerow([link.get('href')])                  
##
##        
##f.close()
