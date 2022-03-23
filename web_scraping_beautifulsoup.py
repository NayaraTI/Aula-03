## Instalar a biblioteca BeautifulSoup

#pip install beautifulsoup4

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Copa_do_Mundo_FIFA').read()
soup = bs.BeautifulSoup(source)

# Pega links e referencias da Pagina
nav = soup.nav

for url in nav.find_all('a'):
    print(url.get('href'))

# Captura elemento do corpo do site

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)


for div in soup.find_all('div', class_='body'):
    print(div.text)

# Capturando tabelas do Site
table = soup.table

table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)



