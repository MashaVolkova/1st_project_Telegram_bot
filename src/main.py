import open_kmbs
#import mind_ua
import bot
import data_base
from threading import Timer

DELAY = 15 #закинула в константу так как юзаю в нескольких местах
timer = None #инициализация переменной таймер


def main():
    start_checking_timer(DELAY)
    data_base.init()


def start_checking_timer(delay): #создание таймера
    global timer
    timer = Timer(delay, check_articles)
    timer.start()


def check_articles():
    global timer
    print('check')
    data_base.add_articles_list(open_kmbs.get_articles().values())
    bot.clear_cache()
    bot.send_articles()

    start_checking_timer(DELAY) #перезапуск таймера


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
