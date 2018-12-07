'''Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the
New York Times homepage.'''


import sys
import requests as rq
from bs4 import BeautifulSoup as bs

for i in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    vid_src = article.find('iframe', class_='youtube-player')['src']
    print(headline,summary,vid_src)
    print()