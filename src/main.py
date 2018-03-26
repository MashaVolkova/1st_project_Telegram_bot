import open_kmbs
#import mind_ua
import bot
import data_base
from threading import Timer

DELAY = 3 #константа, юзаю в нескольких местах
timer = None #инициализирую переменную таймер


def main():
    start_checking_timer(DELAY)
    data_base.init()


def start_checking_timer(delay): #создала таймер
    global timer
    timer = Timer(delay, check_articles)
    timer.start()


def check_articles():
    global timer
    print('check')
    data_base.add_articles_list(open_kmbs.get_articles().values()) #вальюс возвращает массив значений из словаря и добавляет в базу данных
    bot.clear_cache()
    bot.send_articles()

    start_checking_timer(DELAY) #перезапускаю таймер


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
