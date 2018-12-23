'''Use the BeautifulSoup and requests Python packages to print out a list of
all the article titles on the New York Times homepage.'''


import sys
import requests as rq
<<<<<<< HEAD
from bs4 import BeautifulSoup

nyt = 'https://www.nytimes.com/'
nyt_pg = rq.get(nyt)
soup = BeautifulSoup(nyt_pg.text, 'lxml')

#print(soup.prettify())



#trump = soup.find('span', class_ = 'balancedHeadline')

#This, css-6p6lnl, returns the entire block for each article.
#trump = soup.find('div', class_ = 'css-6p6lnl')
#print(trump.prettify())

#this retrieves the blocks for all text
all = soup.find_all('div', class_ = 'css-6p6lnl')
print(all)

#This gets the title of the primary/1st article.
#test = soup.find('h2', class_ = 'css-bzeb53 esl82me2')
#print(test.get_text())


#h2 class




print('done!')
=======
from bs4 import BeautifulSoup as bs

for i in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text
    vid_src = article.find('iframe', class_='youtube-player')['src']
    print(headline,summary,vid_src)
    print()
>>>>>>> 42247ae8d71e2649405ab1584497359121688614
