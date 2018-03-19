from open_kmbs import get_articles
import bot

def main():
    kmbs_articles = get_articles()
    bot.set_articles(kmbs_articles)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()