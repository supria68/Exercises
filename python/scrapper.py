# Let's do some webscrapping!
# I have my travel blog. I want to find out about the places I visited in Germany! 

from bs4 import BeautifulSoup
import requests

source = requests.get('https://nammaprayaana.wordpress.com').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h1.a.text
    print(headline)

    print()

