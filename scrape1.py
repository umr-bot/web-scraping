import requests
import bs4
from bs4 import BeautifulSoup
import re
def scrape(url):
    #url = "https://www.nytimes.com/2020/02/06/movies/cane-river-review.html"
    #html = urllib.urlopen(url).read()
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text,'lxml')
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
    # get text
    text = soup.get_text()
    
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("\n"))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    ret_text = re.findall(r'Review:(.*?)Running',str(text))
    return ret_text
    

