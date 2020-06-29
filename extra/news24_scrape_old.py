import requests
import bs4
from bs4 import BeautifulSoup
import re
url = "https://news24.com"
#html = urllib.urlopen(url).read()
html = requests.get(url)
soup = bs4.BeautifulSoup(html.text,'lxml')

result = soup.find_all()
 #
 ## kill all script and style elements
 #for script in soup(["script", "style"]):
 #    script.extract()    # rip it out
 #
 ## get text
 #text = soup.get_text()
 #
 ## break into lines and remove leading and trailing space on each
 #lines = (line.strip() for line in text.splitlines())
 ## break multi-headlines into a line each
 #chunks = (phrase.strip() for line in lines for phrase in line.split("\n"))
 ## drop blank lines
 #text = '\n'.join(chunk for chunk in chunks if chunk)
 #ret_text = re.findall(r'Review:(.*?)Running',str(text))

 #def GetBodyHTML(soup_file):
 #     tag = soup_file
 #     result = soup_file.find_all("p", "clr_left")
 #     final_result = " "
 #
 #     if len(result) >= 1:
 #         print("many solutions found! :)")
 #         for res in result:
 #             for single in res.find_all(text=True):
 #                 final_result += " "
 #                 print(single.encode("iso-8859-15", "ignore"))
 #                 final_result += single.encode("iso-8859-15", "ignore")
 #     else:
 #         print("no solutions :(")
 #
 #     '''Get the strings in the tag'''
 #
 #     return final_result
 #def GetTextFromWebPages(urls):
 #     text = ""
 #     for url in urls:
 #         source = requests.get(url)
 #         soup = BeautifulSoup(source, "html")
 #         text += " " 
 #         text += GetBodyHTML(soup)
 #         
 #     return text
 #
 #t = GetBodyHTML(soup)
