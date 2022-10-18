import requests
import telebot
from datetime import datetime
from auth_data import token


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    print(f"On {datetime.now().strftime('%y-%m-%d %H-%M')}\nPrice of btc is {sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hi buddy, to see the price type '/price'")


    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if (message.text.lower()) == '/price':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                sell_price = response['btc_usd']['sell']
                bot.send_message(
                    message.chat.id,
                    f"On {datetime.now().strftime('%Y/%m/%d   %H:%M')}\nPrice of btc is  {sell_price}$"
                    )
            except Exception as e:
                print(e)
                bot.send_message(
                    message.chat.id,
                    "Ooops! Something went wrong!"
                    )
        else:
            bot.send_message(message.chat.id, "Проверьте команду и попробуйте еще раз")

    bot.polling()


if __name__ == '__main__':
#   get_data()
    telegram_bot(token)

