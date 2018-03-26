import config
import telebot
import data_base
from threading import Thread


bot = telebot.TeleBot(config.token) #создала объект своего бота
articles_cache = {}
db_session = None

def clear_cache():
    articles_cache = {}


@bot.message_handler(commands=['start'])
def process_start(message):
    user_id = message.chat.id
    if not data_base.is_user_present(user_id):
        data_base.add_user(user_id)

    bot.send_message(user_id, "Use '/set_max {number}' command for set...")

    # global articles
    # if articles is not None:
    #     for article in articles:
    #         text = '{}\n{}\n{}'.format(article.title, article.description, article.id_url)
    #         bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['set_max'])
def set_max_count(message):
    text = message.text.replace('/set_max ', '')
    try:
        max_count = int(text)
        if max_count < 1:
            max_count = 1
        elif max_count > 5:
            max_count = 5
        data_base.update_user_max_count(message.chat.id, max_count)
    except ValueError:
        bot.reply_to(message, 'Wrong input')


def send_articles():
    users = data_base.get_users()
    for user in users:
        if user.last_update not in articles_cache:
            arts = data_base.get_articles_by_timestamp(user.last_update)
        else:
            arts = articles_cache[user.last_update]

        if len(arts) > 0:
            data_base.update_user_last_update(user.id, arts[0].timestamp)
            arts = arts[:user.max_count]
            for article in arts:
                text = '{}\n{}\n{}'.format(article.title, article.description, article.id_url)
                bot.send_message(user.id, text)



def run_bot(): #функция которая запускается в отдельном потоке
    bot.polling(none_stop=True)
    
    
thread = Thread(target=run_bot)#запуск функции
thread.start()
