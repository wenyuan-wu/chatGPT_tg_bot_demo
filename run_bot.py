import os
import telebot
from openai_res import get_response_openai, get_response_openai_test

max_turns = 20
history = []
turns = 0


def run_tg_bot(bot_token):
    """
    Function to initialize the bot.
    :param bot_token: environment variable BOT_TOKEN
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
        global turns, history
        # Keep track of conversation history
        if not history:
            history.append({"role": "system", "content": "You are a helpful assistant."})
        if message.text == "/new":
            # Reset history and turn counter
            history = []
            turns = 0
            bot.send_message(message.chat.id,
                             "Start new conversation")
        else:
            # Add user message to history
            history.append({"role": "user", "content": message.text})
            prompt = history
            reply = get_response_openai(prompt)
            history.append({"role": "assistant", "content": reply})
            bot.reply_to(message, reply)
            turns += 1

            # Check if maximum turns has been reached
            if turns >= max_turns:
                # Send message to user to indicate maximum turns has been reached
                bot.send_message(message.chat.id,
                                 "This conversation has ended as the maximum number of turns has been reached.")

                # Reset history and turn counter
                history = []
                turns = 0

            # Send message to user to indicate number of turns left
            elif turns >= max_turns - 5:
                remaining_turns = max_turns - turns
                bot.send_message(message.chat.id, f"{remaining_turns} turns left in this conversation.")

    bot.infinity_polling()


def main():
    bot_token = os.environ.get('BOT_TOKEN')
    run_tg_bot(bot_token)
    # run_tg_bot(bot_token, test=True)


if __name__ == '__main__':
    main()
