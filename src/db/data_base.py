from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from time import time


Base = declarative_base()
engine = None
session = None


class Articles(Base):
    __tablename__ = 'articles'
    id_url = Column(String(1000), primary_key=True)
    title = Column(String(500), nullable=False)
    description = Column(String(500), nullable=True)
    timestamp = Column(Integer)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    update_period = Column(Integer)
    last_update = Column(Integer)
    max_count = Column(Integer)


def init():
    global engine, session
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
        # try:
        if not is_article_present(article['url']):
            add_article(article['url'], article['title'], article['description'], article['time'])
        # except:
        #     print('Error when added to data base')



def get_articles(time_offset=86400):
    time_threshold = round(time()) - time_offset
    arts = session.query(Articles).filter(Articles.timestamp >= time_threshold).all()[:3]
    return arts


def get_articles_for_timestamp(timestamp):
    arts = session.query(Articles).filter(Articles.timestamp >= timestamp).all()
    return arts


def is_article_present(art_id):
    if art_id is not None:
        return session.query(Articles).filter(Articles.id_url == art_id) is not None
    else:
        return len(session.query(Articles).all()) > 0


def add_user(user_id, update_period=1, max_count=1):
    user = User()
    user.id = user_id
    user.update_period = update_period
    user.max_count = max_count
    user.timestamp = 0
    session.add(user)
    session.commit()


def is_user_present(user_id):
    user = session.query(User).filter(User.id == user_id).all()
    return user is not None

def get_users():
    return session.query(User).all()
