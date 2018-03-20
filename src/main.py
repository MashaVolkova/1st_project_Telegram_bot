import open_kmbs
import mind_ua
import bot

def main():
    kmbs_articles = open_kmbs.get_articles()
    mind_ua_articles = mind_ua.get_articles()
    bot.set_articles(kmbs_articles)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()