import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html'

data = requests.get(url)

soup = BeautifulSoup(data.content, 'html.parser')
title = soup.h1.get_text()
print("Article title: ", title)
for content in soup.find_all('p'):
    print(content.get_text())