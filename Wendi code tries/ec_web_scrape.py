import requests
from bs4 import BeautifulSoup

URL = 'https://www.census.gov/programs-surveys/popest.html'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    print(job_elem, end='\n'*2)


