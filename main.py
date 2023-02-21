import telepot
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")


bot = telepot.Bot(token=token)


# Define a function to handle incoming messages
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        message_text = msg['text']
        if message_text == '/chatid':
            bot.sendMessage(chat_id, 'Your chat ID is: ' + str(chat_id))
        if message_text == "/start":
            bot.sendMessage(
                chat_id, """Welcome to the REANALYSIS System... Type "/steps" to know how to enable this bot for you.""")
        if message_text == "/steps":
            bot.sendMessage(chat_id, """Steps to get reports through this bot \n\n 1. Type /chatid command to get get your chat id which you have to enter during registsration process of REANALYSIS desktop application.\n\n 2. Enter the 10 digit chat id which you get from this bot in REANALYSIS desktop application during sign up process \n\n 3. Done... Now you can get all updates regarding the REANALYSIS desktop application throgh this bot.""")


# start the bot and set up the message handler for the /start command
bot.message_loop({'chat': handle_message}, run_forever=True)
