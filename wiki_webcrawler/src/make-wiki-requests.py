import requests
from bs4 import BeautifulSoup
#from requests import *

response = requests.get('https://en.wikipedia.org/wiki/Arthur_Wellesley,_1st_Duke_of_Wellington')
# response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
# response = requests.get('https://en.wikipedia.org')
req_html = response.text
soup = BeautifulSoup(req_html,'html.parser')
print(soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a.get('href'))

#print(response.text)
#print(type(response.text))