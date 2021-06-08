import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

url="https://www.census.gov/programs-surveys/popest"

r=requests.get(url)
soup= BeautifulSoup(r.content, "html.parser")

results =  soup.find_all("a")

for link in results:
    link.get("href")       

def unique_urls(tags,url):
    #cleaned_urls = set()
    list_of_urls = ['url_1', 'url_1', 'url_2', 'url_1', 'url_1', 'url_2', 'url_3', 'url_3'] 
    set_of_urls = set(list_of_urls) # return : {'url_1', 'url_2', 'url_3'}
    list_clean = list(set_of_urls) # return :['url_3', 'url_1', 'url_2']
    for link in results:
        link = link.get("href")

        if link is None:
            continue
        if link.endswith('/'):
            link = link[:-1]

    actual_url = urllib.parse.urljoin(url,link)
    cleaned_urls.add(actual_url)

    return cleaned_urls

    print(cleaned_urls)


import csv
for link in results:
    S=link.get('href')
    csvRow = [S]
    csvfile = "urls1.csv"
with open(csvfile, "a") as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(csvRow )
