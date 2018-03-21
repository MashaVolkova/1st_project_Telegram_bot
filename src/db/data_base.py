from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from time import time


Base = declarative_base()


class Articles(Base):
    __tablename__ = 'articles'
    id_url = Column(String(1000), primary_key=True)
    title = Column(String(500), nullable=False)
    description = Column(String(500), nullable=True)
    timestamp = Column(Integer)


engine = create_engine('sqlite:///articles.db')

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine) #создаю класс
session = Session() #создаю экземпляр класса


def add_article(id_url, title, description, timestamp): #добавляю одну запись в базу данных
    article = Articles()
    article.id_url, article.title, article.description, article.timestamp = id_url, title, description, timestamp
    session.add(article)
    session.commit()


def add_articles_list(articles): #если нужно добавить список записей
    for article in articles:
        add_article(article['url'], article['title'], article['description'], article['time'])


def get_articles(time_offset = 86400):
    time_threshold = round(time()) - time_offset
    arts = session.query(Articles).filter(Articles.timestamp >= time_threshold).all()[:3]
    return arts


def is_article_present():
    return len(session.query(Articles).all()) > 0