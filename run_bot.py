import os
import telebot
from openai_res import get_response_openai, get_response_openai_test, get_settings
from dotenv import load_dotenv

max_turns = 20
conversations = {}  # Dictionary to store the conversation history for each user


def run_tg_bot(bot_token, settings):
    """
    Function to initialize the bot.
    :param bot_token: environment variable BOT_TOKEN
    :return: None
    """
    bot = telebot.TeleBot(bot_token)
    welcome_msg = settings["welcome_message"]
    sys_prompt = settings["system_prompt"]
    help_msg = settings["help_message"]
    new_msg = settings["new_message"]


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, welcome_msg, parse_mode="Markdown")

    @bot.message_handler(commands=['help'])
    def send_welcome(message):
        bot.reply_to(message, help_msg)

    @bot.message_handler(func=lambda msg: True)
    def respond_openai(message):
        chat_id = message.chat.id
        global conversations, max_turns

        # Initialize conversation history for new user
        if chat_id not in conversations:
            conversations[chat_id] = []
            conversations[chat_id].append({"role": "system", "content": sys_prompt})

        # Start new conversation if user types /new
        if message.text == "/new":
            conversations[chat_id] = []
            conversations[chat_id].append({"role": "system", "content": sys_prompt})
            bot.send_message(chat_id, new_msg)
        else:
            # Add user message to conversation history
            conversations[chat_id].append({"role": "user", "content": message.text})

            # Get AI generated response
            prompt = conversations[chat_id]
            reply = get_response_openai(prompt, settings)

            # Add AI generated response to conversation history
            conversations[chat_id].append({"role": "assistant", "content": reply})

            # Send AI generated response to user
            bot.reply_to(message, reply, parse_mode="Markdown")

            # Check if maximum turns has been reached
            if len(conversations[chat_id]) // 2 >= max_turns:
                # Send message to user to indicate maximum turns has been reached
                bot.send_message(chat_id,
                                 "This conversation has ended as the maximum number of turns has been reached.")

                # Reset conversation history for this user
                conversations[chat_id] = []
            elif len(conversations[chat_id]) // 2 >= max_turns - 5:
                remaining_turns = max_turns - len(conversations[chat_id]) // 2
                bot.send_message(chat_id, f"{remaining_turns} turns left in this conversation. "
                                          f"To start a new conversation, type /new.")

    bot.infinity_polling()


def main():
    load_dotenv()
    bot_token = os.environ.get('BOT_TOKEN')
    yaml_file = "./prompts.yaml"
    settings = get_settings(yaml_file)
    run_tg_bot(bot_token, settings)


if __name__ == '__main__':
    main()
