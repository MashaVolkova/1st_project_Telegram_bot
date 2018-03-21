import open_kmbs
#import mind_ua
import bot
import data_base


def main():
    if not data_base.is_article_present():
        data_base.add_articles_list(open_kmbs.get_articles().values())

    articles_from_db = data_base.get_articles()
    bot.set_articles(articles_from_db)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()