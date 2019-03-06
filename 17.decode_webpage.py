'''Use the BeautifulSoup and requests Python packages to print out a list of
all the article titles on the New York Times homepage.'''


import sys
import requests as rq
from bs4 import BeautifulSoup

nyt = 'https://www.nytimes.com'
nyt_pg = rq.get(nyt)
soup = BeautifulSoup(nyt_pg.text)




for story_heading in soup.find_all(class_="css-bzeb53 esl82me2"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())


"""
for i in soup.find_all('css-bzeb53 esl82me2'):
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    vid_src = article.find('iframe', class_='youtube-player')['src']
    print(headline,summary,vid_src)
    print()
"""
print('done!')
