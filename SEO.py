from bs4 import BeautifulSoup
import requests


source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')


for article in soup.find_all('article'):
    headline = article.h2.a.text.split()

    summary = article.find('div', class_='entry-content').p.text.split()

x = input("enter the word to be found in the headline :")
a = input("enter the word to be found in the summary :")
k = 0
q = 0
for z in headline:
    if x == z:
        k = k + 1

for t in summary:
    if a == t:
        q = q + 1

print("the word",x,"is found",k,"times")
print("the word",a,"is found",q,"times")
