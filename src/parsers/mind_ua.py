import requests
import time
from bs4 import BeautifulSoup


def process_article(article):
    url = article.a['href']
    article__title = article.a.text
    article__subtitle = article.find('div', {'class': 'article__subtitle'}).text
    return url, article__title, article__subtitle


def get_articles():
    r = requests.get('https://mind.ua/education/publications')
    soup = BeautifulSoup(r.content, 'html.parser')  # файл, который скачали передаем в бьютифул суп

    article_content = soup.find('div', {'class': 'block_list__inner'})
    articles = article_content.findAll('div', {'class': 'article__content'})

    article_dict = {}

    for article in articles:
        url, article__title, article__subtitle = process_article(article)
        if url not in article_dict:
            article_dict[url] = {
                'article__title': article__title,
                'url': url,
                'article__subtitle': article__subtitle,
                'time': time.time()
                # тайм штамп - значение в секундах, описывает момент времени когда статья была обработана и добавлена в словарь
            }
    return article_dict
