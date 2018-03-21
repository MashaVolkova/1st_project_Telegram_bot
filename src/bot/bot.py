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
    global articles
    if articles is not None:
        for article in articles:
            text = '{}\n{}\n{}'.format(article.title, article.description, article.id_url)
            bot.send_message(message.chat.id, text)


def run_bot(): #функция которая запускается в отдельном потоке
    bot.polling(none_stop=True)
    
    
thread = Thread(target=run_bot)#запуск функции
thread.start()
