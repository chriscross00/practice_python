# https://djangostars.com/blog/list-comprehensions-and-generator-expressions/

import requests as rq
from bs4 import BeautifulSoup


page = rq.get('http://dataquestio.github.io/web-scraping-pages/simple'
                    '.html')
soup = BeautifulSoup(page.content, 'html.parser')

print([type(item) for item in list(soup.children)])