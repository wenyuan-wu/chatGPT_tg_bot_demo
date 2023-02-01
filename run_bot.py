import os
import telebot
from openai_res import get_response_openai, get_response_openai_test


def run_tg_bot(bot_token, test=False):
    """
    Function to initialize the bot.
    :param bot_token: environment variable BOT_TOKEN
    :param test: if this is a test
    :return: None
    """
    bot = telebot.TeleBot(bot_token)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        text = "Hello, this is a tiny demo for a ChatGPT-like conversational agent.\nSimply type any message to get " \
               "a AI generated reply.\ne.g. 'What is quantum computing?'"
        bot.send_message(message.chat.id, text, parse_mode="Markdown")

    # function to echo input message
    # @bot.message_handler(func=lambda msg: True)
    # def echo_all(message):
    #     bot.reply_to(message, message.text)

    @bot.message_handler(func=lambda msg: True)
    def respond_openai(message):
        prompt = message.text
        if test:
            reply = get_response_openai_test(prompt)
        else:
            reply = get_response_openai(prompt)
        bot.reply_to(message, reply)

    bot.infinity_polling()


def main():
    bot_token = os.environ.get('BOT_TOKEN')
    run_tg_bot(bot_token)
    # run_tg_bot(bot_token, test=True)


if __name__ == '__main__':
    main()
