import requests
import time
from bs4 import BeautifulSoup


def process_li(article):
    url = ''
    title = ''
    description = ''
    for child in article.children:
        if child.name == 'a':
            url = child['href']
            title = child.text
        elif child.name == 'p':
            description = child.text
    return url, title, description


def get_articles():
    r = requests.get('http://open.kmbs.ua/ua/articles/index.html')
    soup = BeautifulSoup(r.content, 'html.parser')  # файл, который скачали передаем в бьютифул суп

    ul = soup.find('ul', {'class': 'b-listing-list'})
    lis = ul.findAll('li', {'class': 'item'})

    article_dict = {}

    for li in lis:
        url, title, description = process_li(li)
    if url not in article_dict:
        article_dict[url] = {
            'title': title,
            'url': url,
            'description': description,
            'time': time.time()
            # тайм штамп - значение в секундах, описывает момент времени когда статья была обработана и добавлена в словарь
        }
    return article_dict
