import config
import telebot
from threading import Thread


bot = telebot.TeleBot(config.token) #создала объект своего бота
articles = None


def set_articles(art):
    global articles
    articles = art

@bot.message_handler(commands=['start'])
def send_articles(message):
    if articles is not None:
        limit = 1
        i = 0
        for url in articles:
            if i >= limit:
                break
            text = '{}\n{}\n{}'.format(articles[url]['title'], articles[url]['description'], url)
            bot.send_message(message.chat.id, text)
            i += 1


def run_bot(): #функция которая запускается в отдельном потоке
    bot.polling(none_stop=True)
    
    
thread = Thread(target=run_bot)#запуск функции
thread.start()
