# Telegram Bot - Multi Turn Conversation

A telegram bot to handle conversation for multiple turn with OpenAI API. 
This is mostly not purpose-built, e.g., a Chatbot.
Also check this [repo](https://github.com/wenyuan-wu/tg_bot_single)

## Setting up environment

```commandline
pip install telebot
pip install openai
pip install python-dotenv
pip install pyyaml
```

## Dot env file

It needs two keys: `BOT_TOKEN` and `OPENAI_API`

## YAML settings example

Default location: `./prompts.yaml`

```yaml
---
model_engine: "gpt-4o-mini"
system_prompt: "You are a helpful assistant."
welcome_message: "Hello, this is a tiny demo for a ChatGPT-like conversational agent.\nSimply type any message to get a AI generated reply.\ne.g. 'What is quantum computing?"
help_message: "Just try anything ..."
```

## Bash script

The bash script automatically appends the PID to `output.log`, to make it easier to determine which process to terminate. It is still good practice to check the PID manually:

```commandline
ps -ef | grep "python"
kill -9 Python_PID
```


based on:
https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/

and

https://medium.com/@alexandre.tkint/revolutionize-your-chatbot-game-with-the-chat-gpt-api-and-python-get-started-in-just-3-minutes-8b588dacf48f

icon: https://creator.nightcafe.studio/creation/SafPI8ml79S7sF5Db0qL
