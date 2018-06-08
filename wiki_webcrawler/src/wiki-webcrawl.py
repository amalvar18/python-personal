import requests
from bs4 import BeautifulSoup
import time
import urllib

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

# TODO: Implement the continue_crawl function described above
def continue_crawl(search_history, target_url):
    continue_flag = True
    if(search_history[-1] == target_url):
        print("Target and most recent article are the same")
        continue_flag = False
    elif(len(search_history) > 35):
        print("More than 25 urls long")
        continue_flag = False
    # elif(target_url in search_history):
    elif(len(search_history) != len(set(search_history))):
        print("List has a cycle in it")
        continue_flag = False
    else:
        continue_flag = True 
    return continue_flag
    
def find_first_link(start_url):
    # return the first link as a string, or return None if there is no link
    article_link = None
    response = requests.get(start_url)
    response_html = response.text
    soup = BeautifulSoup(response_html,'html.parser')
    
    # This div contains the article's body
    # Body nested in two div tags
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    
    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
            
    if not article_link:
        return
        
     # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    
    return first_link
    
# search_history = ['https://en.wikipedia.org/wiki/Floating_point',
# 'https://en.wikipedia.org/wiki/Philosophy',
# 'https://en.wikipedia.org/wiki/Dead_Parrot_sketch',
# 'https://en.wikipedia.org/wiki/CoalHouse_Fort']

#target_url = 'https://en.wikipedia.org/wiki/Philosophy'

# print(continue_crawl(search_history, target_url)) 

article_chain = [start_url]
# article_chain = ['https://en.wikipedia.org/wiki/Deadpool']

#print(find_first_link(article_chain[-1]))

def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        print(article_chain[-1])
        first_link = find_first_link(article_chain[-1])
        if not first_link:
            print("We've arrived at an article with no links, aborting search!")
            break

        # add the first link to article_chain
        article_chain.append(first_link)
        # delay for about two seconds
        time.sleep(2)
        
web_crawl()