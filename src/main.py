import open_kmbs
#import mind_ua
import bot
import data_base
from threading import Timer

timer = None


def main():
    global timer
    timer = Timer(1, check_articles)
    timer.start()
    data_base.init()


def check_articles():
    global timer
    # if timer.interval == 0:
    #     timer.interval = 10
    data_base.add_articles_list(open_kmbs.get_articles().values())
    bot.clear_cache()
    bot.send_articles()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
