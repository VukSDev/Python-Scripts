from lxml import html
import requests

page = requests.get('https://www.brainyquote.com/topics/life')
tree = html.fromstring(page.content)

authors = tree.xpath('//a[@title="view author"]/text()')
quotes = tree.xpath('//a[@title="view quote"]/text()')

f = open("quotes.txt", "w+")

def StoreData():
    for i, j in zip(quotes, authors):
        f.write(i + " - " + j + "\n \n")

def PrintData():
    print('Authors: ', authors)
    print('Quotes: ', quotes)

StoreData()
# PrintData()
