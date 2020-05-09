from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests
import time

def get_image(chapter_soup):
    for first_div in  chapter_soup.find_all('img'):
        try:
            if(first_div['src'].startswith('https')):
                return (first_div['src'])
        except:
            pass
#Make Firefox Window open in background
options = Options()
options.add_argument('--headless')
browser = webdriver.Firefox(options=options)

url = 'https://mangadex.org/chapter/883836/1'
r = requests.get(url)

browser.get(url)

time.sleep(4)   #wait for page to load
html = browser.page_source
#Trying to get the Image
chapter_soup = BeautifulSoup(html,'lxml')
a = get_image(chapter_soup)
browser.quit()
print(a)
#Saving the HTML to compare
# with open('chapter.txt','w', encoding="utf-8") as htmlFile:
    # htmlFile.write(html)
# with open('chapterRequests.txt','w', encoding="utf-8") as requestsFile:
    # requestsFile.write(r.text)
