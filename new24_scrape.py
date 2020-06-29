import requests
import bs4
from bs4 import BeautifulSoup
import re

def scrape_24(url):
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
     #ret_text = re.findall(r'Review:(.*?)Running',str(text))
     return text

url='https://www.news24.com'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
data=soup.find({'div','a'},class_='tab-wrapper')
 #o = 1;
 #if(o == 1):
 #    print(1) 
 #else:
top_read = data.find('a').get('href')

#Get text of top_read link
r2=requests.get(top_read)
soup2=BeautifulSoup(r2.text,'html.parser')
#data2=soup2.find({'p'},class_='clr_left')
d = soup2.find('article')
story = ""
#Get title of top_story
article_details = soup2.find(class_='article_details')
top_story_title = article_details.find('h1').text #OR article_details.find(class_="bold").text
print("Top article title: "+top_story_title)
print()
for m in d.stripped_strings:
    story += m
    print(m)


