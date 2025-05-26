import os
import json
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv('TOKEN')
CHANNEL = os.getenv('CHANNEL')

if not TOKEN or not CHANNEL:
    print("Ошибка: Не заданы переменные окружения TOKEN или CHANNEL")
    exit(1)

bot = Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text("Привет! Я SkyFreeLanc Bot.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
