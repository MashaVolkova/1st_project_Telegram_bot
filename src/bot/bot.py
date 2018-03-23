import config
import telebot
import data_base
from threading import Thread


bot = telebot.TeleBot(config.token) #создала объект своего бота
articles_cache = {}


def clear_cache():
    articles_cache = {}


@bot.message_handler(commands=['start'])
def process_start(message):
    user_id = message.chat.id
    if not data_base.is_user_present(user_id):
        data_base.add_user(user_id)

    # global articles
    # if articles is not None:
    #     for article in articles:
    #         text = '{}\n{}\n{}'.format(article.title, article.description, article.id_url)
    #         bot.send_message(message.chat.id, text)


def send_articles():
    users = data_base.get_users()
    for user in users:
        if user.timestamp not in articles_cache:
            arts = data_base.get_articles_for_timestamp(user.timestamp)
        else:
            arts = articles_cache[user.timestamp]
        for article in arts:
            text = '{}\n{}\n{}'.format(article.title, article.description, article.id_url)
            bot.send_message(user.id, text)



def run_bot(): #функция которая запускается в отдельном потоке
    bot.polling(none_stop=True)
    
    
thread = Thread(target=run_bot)#запуск функции
thread.start()
